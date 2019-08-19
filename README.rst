DSSPparser
==========

|PyPI - Version| |PyPI - Python Version| |GitHub - LICENSE|

DSSPparser is an easy tool to parse dssp file, and can transform PDB
format file to dssp format file by
`xssp <http://www.cmbi.ru.nl/xssp/api/>`__,also support the tansfrom
between the PDB id and dssp format, hssp format and sequence.

Install
-------

.. code-block::

    pip install DSSPparser


Examples
--------

parse dssp file to pandas.dataframe

.. code-block::

    from DSSParser import parseDSSP
    parser = parseDSSP('2GW9.dssp')
    parser.parse()
    pddict = parser.dictTodataframe()

Transform between the PDB format and dssp format

.. code-block::

    from DSSPparser import pdbToxssp
    result = pdbToxssp("2GW9")

License
-------

Released under the MIT license.

.. |PyPI - Version| image:: https://img.shields.io/pypi/v/DSSPparser.svg?style=flat
   :target: https://pypi.org/project/DSSPparser/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/DSSPparser.svg
   :target: https://pypi.org/project/DSSPparser/
.. |GitHub - LICENSE| image:: https://img.shields.io/github/license/neolei/DSSPparser.svg?style=flat
   :target: ./LICENSE.txt
