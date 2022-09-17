# This example client takes a PDB file, sends it to the REST service, which
# creates HSSP data. The HSSP data is then output to the console.
# api by https://github.com/cmbi/xssp-api/blob/master/xssp_api/frontend/api/endpoints.py


import json
import requests
import time
import os
from Bio.PDB.PDBList import PDBList
import shutil

REST_URL = "https://www3.cmbi.umcn.nl/xssp/"

inputCollection = ["pdb_id", "pdb_redo_id", "pdb_file", "sequence"]
outputCollection = ["hssp_hssp", "hssp_stockholm", "dssp"]

def pdbToxssp_local(_input, inputF="pdb", output_dir='./'):
    '''transform PDB to xssp
    
    Arguments:
        _input {str} -- PDB id
    
    Keyword Arguments:
        inputF {str} -- input format (default: {"pdb"})
    '''
    pdbl = PDBList()
    native_pdb = pdbl.retrieve_pdb_file(_input, pdir=output_dir, file_format=inputF)
    if shutil.which('mkdssp'):
        command = f"mkdssp -i {native_pdb} -o {_input}.dssp"
        os.system(command)
    else:
        print("Please install the DSSP software! <conda install -c salilab dssp>")
        exit()

def pdbToxssp(_input, inputF="pdb_id", outputF="dssp"):
    '''transform PDB to xssp
    
    Arguments:
        _input {str} -- input id or PDB file
    
    Keyword Arguments:
        inputF {str} -- input format (default: {"pdb_id"})
        outputF {str} -- output format (default: {"dssp"})
    
    Raises:
        Exception -- raise format error
    
    Returns:
        str -- dssp or hssp format
    '''

    # inuptF type check
    if inputF not in inputCollection:
        raise "input Format error, Please check your format!"

    if outputF not in outputCollection:
        raise "output Format error, Please check your format!"

    # request url
    url_create = '{0}api/create/{1}/{2}/'.format(REST_URL, inputF, outputF)

    if inputF == "pdb_id":
        pdb_id = {"data": _input}
        r = requests.post(url_create, data=pdb_id)
    elif inputF == "pdb_file":
        files = {'file_': open(_input, 'rb')}
        r = requests.post(url_create, files=files)
    elif inputF == "pdb_redo_id":
        pdb_redo_id = {"data": _input}
        r = requests.post(url_create, data=pdb_redo_id)
    elif inputF == "sequence":
        sequence = {"data": open(_input, 'rb')}
        r = requests.post(url_create, data=sequence)

    # Send a request to the server to create hssp data from the pdb file data.
    # If an error occurs, an exception is raised and the program exits. If the
    # request is successful, the id of the job running on the server is
    # returned.
    r.raise_for_status()

    job_id = json.loads(r.text)['id']
    print("Job submitted successfully. Id is: '{}'".format(job_id))

    # Loop until the job running on the server has finished, either successfully
    # or due to an error.
    ready = False
    while not ready:
        # Check the status of the running job. If an error occurs an exception
        # is raised and the program exits. If the request is successful, the
        # status is returned.
        url_status = '{0}api/status/{1}/{2}/{3}/'.format(
            REST_URL, inputF, outputF, job_id)
        r = requests.get(url_status)
        r.raise_for_status()

        status = json.loads(r.text)['status']
        print("Job status is: '{}'".format(status))

        # If the status equals SUCCESS, exit out of the loop by changing the
        # condition ready. This causes the code to drop into the `else` block
        # below.
        #
        # If the status equals either FAILURE or REVOKED, an exception is raised
        # containing the error message. The program exits.
        #
        # Otherwise, wait for five seconds and start at the beginning of the
        # loop again.
        if status == 'SUCCESS':
            ready = True
        elif status in ['FAILURE', 'REVOKED']:
            raise Exception(json.loads(r.text)['message'])
        else:
            time.sleep(5)
    else:
        # Requests the result of the job. If an error occurs an exception is
        # raised and the program exits. If the request is successful, the result
        # is returned.
        url_result = '{0}api/result/{1}/{2}/{3}/'.format(
            REST_URL, inputF, outputF, job_id)
        r = requests.get(url_result)
        r.raise_for_status()
        result = json.loads(r.text)['result']

        # Return the result to the caller, which prints it to the screen.
        return result


if __name__ == '__main__':
    result = pdbToxssp("2GW9")
    print(result)
