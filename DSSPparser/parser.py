# dssp file from http://www.cmbi.ru.nl/xssp/
# parse protein secondary structure
# reference by https://github.com/wilkelab/ProteinEvolutionToolbox/blob/master/python/dssp_parse.py
# dssp format description in the https://swift.cmbi.umcn.nl/gv/dssp/DSSP_3.html
# https://swift.cmbi.umcn.nl/gv/dssp/HTML/format.html


import re
import pandas as pd


class parseDSSP(object):
    '''parse dssp file
    Arguments:
        file {str} -- dssp file path
    '''

    def __init__(self, file):
        # sequential residue number
        self.resnum = []
        # original PDB resname
        self.inscode = []
        self.chain = []
        self.aa = []
        self.struct = []
        self.structdetails = []
        self.bp1 = []
        self.bp2 = []
        self.acc = []
        self.h_nho1 = []
        self.h_ohn1 = []
        self.h_nho2 = []
        self.h_ohn2 = []
        self.tco = []
        self.kappa = []
        self.alpha = []
        self.phi = []
        self.psi = []
        self.xca = []
        self.yca = []
        self.zca = []
        self.rcsb_given_chain = []
        self.author_given_chain = []
        self._file = file

    def parse(self):
        ''' parse line by line '''
        input_handle = open(self._file, 'r')
        flag = False
        for line in input_handle:
            if (re.search('#', line)):
                flag = True
                continue
            if flag:
                # RESIDUE
                self.resnum.append(line[0:5].strip())
                self.inscode.append(line[5:10].strip())
                self.chain.append(line[10:12].strip())
                # AA
                self.aa.append(line[12:14].strip())
                # S
                self.struct.append(line[14:17])
                self.structdetails.append(line[16:24])

                self.bp1.append(line[24:29].strip())
                self.bp2.append(line[29:34].strip())
                # solvent accessibility
                self.acc.append(line[34:38].strip())
                # hydrogen bonds
                self.h_nho1.append(line[38:50].strip())
                self.h_ohn1.append(line[50:61].strip())
                self.h_nho2.append(line[61:72].strip())
                self.h_ohn2.append(line[72:83].strip())

                self.tco.append(line[83:91].strip())

                self.kappa.append(line[91:97].strip())
                self.alpha.append(line[97:103].strip())
                # IUPAC peptide backbone torsion angles
                self.phi.append(line[103:109].strip())
                self.psi.append(line[109:115].strip())
                # author_given_chain
                self.xca.append(line[115:122].strip())
                self.yca.append(line[122:129].strip())
                self.zca.append(line[129:136].strip())
                # CHAIN AUTHCHAIN
                self.rcsb_given_chain.append(line[136:153].strip())
                self.author_given_chain.append(line[153:].strip())

    def dictTodataframe(self):
        ''' dict to dataframe
        
        Returns:
            pandas.dataframe -- dataframe foramt 
        '''

        _dict = {'resnum': self.resnum, 'inscode': self.inscode, 'chain': self.chain, 'aa': self.aa,
                 'struct': self.struct, 'structdetails': self.structdetails,
                 'bp1': self.bp1, 'bp2': self.bp2, 'acc': self.acc, 'h_nho1': self.h_nho1, 'h_ohn1': self.h_ohn1,
                 'h_nho2': self.h_nho2, 'h_ohn2': self.h_ohn2,
                 'tco': self.tco, 'kappa': self.kappa, 'alpha': self.alpha, 'phi': self.phi, 'psi': self.psi,
                 'xca': self.xca, 'yca': self.yca, 'zca': self.zca,
                 'rcsb_given_chain': self.rcsb_given_chain, 'author_given_chain': self.author_given_chain}
        df = pd.DataFrame.from_dict(_dict)
        return df

    @property
    def getResnums(self):
        '''sequential resnumber, including chain breaks as extra residues
        
        Returns:
            list -- resnums
        '''

        return self.resnum

    @property
    def getInsCode(self):
        '''original PDB resname, not nec. sequential, may contain letters
        
        Returns:
            list -- inscode
        '''

        return self.inscode

    @property
    def getChain(self):
        '''one-letter chain ID, if any
        
        Returns:
            list -- chain
        '''

        return self.chain

    @property
    def getAAs(self):
        ''' amino acid sequence in one letter code
        
        Returns:
            list -- aa
        '''

        return self.aa

    @property
    def getSecStruc(self):
        '''secondary structure
        
        Returns:
            list -- secstruc
        '''

        return self.struct

    @property
    def getSecStrucDetail(self):
        '''3-turns/helix,4-turns/helix,5-turns/helix,geometrical bend,chirality,beta bridge label,beta bridge label
        
        Returns:
            list -- secondary structure details
        '''

        return self.structdetails

    @property
    def getBP1(self):
        '''beta bridge partner resnum
        
        Returns:
            list -- bp1
        '''

        return self.bp1

    @property
    def getBP2(self):
        '''beta bridge partner resnum,beta sheet label
        
        Returns:
            list -- bp2
        '''

        return self.bp2

    @property
    def getACC(self):
        '''solvent accessibility
        
        Returns:
            list -- acc
        '''

        return self.acc

    @property
    def getH_NHO1(self):
        '''hydrogen bonds
        
        Returns:
            list -- h_nho1
        '''

        return self.h_nho1

    @property
    def getH_NHO2(self):
        '''hydrogen bonds
        
        Returns:
            list -- h_nho2
        '''

        return self.h_nho2

    @property
    def getH_OHN1(self):
        '''hydrogen bonds
        
        Returns:
            list -- h_ohn1
        '''

        return self.h_ohn1

    @property
    def getH_OHN2(self):
        '''hydrogen bonds
        
        Returns:
            list -- h_ohn2
        '''

        return self.h_ohn2

    @property
    def getTCO(self):
        '''cosine of angle between C=O of residue I and C=O of residue I-1. For alpha-helices,TCO is near +1, for beita-sheets TCO is near -1. Not used for structure definition.
        
        Returns:
            list -- tco
        '''

        return self.tco

    @property
    def getKAPPA(self):
        '''virtual bond angle (bend angle) defined by the three C atoms of residues I-2,I,I+2.Used to define bend (structure code 'S').
        
        Returns:
            list -- [description]
        '''

        return self.kappa

    @property
    def getALPHA(self):
        '''virtual torsion angle (dihedral angle) defined by the four C atoms of residues I-1,I,I+1,I+2.Used to define chirality (structure code '+' or '-').
        
        Returns:
            list -- alpha
        '''

        return self.alpha

    @property
    def getPHI(self):
        '''IUPAC peptide backbone torsion angles
        
        Returns:
            list -- phi
        '''

        return self.phi

    @property
    def getPSI(self):
        '''IUPAC peptide backbone torsion angles
        
        Returns:
            list -- psi
        '''

        return self.psi

    @property
    def getX(self):
        '''echo of C atom coordinates

        Returns:
            list -- xca
        '''

        return self.xca

    @property
    def getY(self):
        '''echo of C atom coordinates
        
        Returns:
            list -- yca
        '''

        return self.yca

    @property
    def getZ(self):
        '''echo of C atom coordinates
        
        Returns:
            list -- zca
        '''

        return self.zca

    @property
    def getRcsbChain(self):
        '''The rcsb-given and author-given chain ids respectively.
        These will be the same for PDB files, but different for mmCIF files.
        Also, in mmCIF files these ids can be longer than one character.

        Returns:
            list -- rcsb_given_chain
        '''

        return self.rcsb_given_chain

    @property
    def getAuthChain(self):
        '''The rcsb-given and author-given chain ids respectively.
        These will be the same for PDB files, but different for mmCIF files.
        Also, in mmCIF files these ids can be longer than one character.
        
        Returns:
            list -- author_given_chain
        '''

        return self.author_given_chain


if __name__ == '__main__':
    import sys
    parse_ = parseDSSP(sys.argv[1])
    parse_.parse()
    print(parse_.getACC)
