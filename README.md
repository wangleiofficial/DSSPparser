# DSSPparser

[![PyPI - Version](https://img.shields.io/pypi/v/DSSPparser.svg?style=flat)](https://pypi.org/project/DSSPparser/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DSSPparser.svg)](https://pypi.org/project/DSSPparser/)
[![GitHub - LICENSE](https://img.shields.io/github/license/neolei/DSSPparser.svg?style=flat)](./LICENSE.txt)
[![Build Status](https://travis-ci.org/neolei/DSSPparser.svg?branch=master)](https://travis-ci.org/neolei/DSSPparser)
[![codecov](https://codecov.io/gh/neolei/DSSPparser/branch/master/graph/badge.svg)](https://codecov.io/gh/neolei/DSSPparser)


DSSPparser is an easy tool to parse dssp file, and can transform PDB format file to dssp format file by [xssp](http://www.cmbi.ru.nl/xssp/api/),also support the tansfrom between the PDB id and dssp format, hssp format and sequence.

## Install 
stabel verison
```
pip install DSSPparser
```
lastest version

```
pip install git+https://github.com/neolei/DSSPparser.git@master
```

## Examples

parse dssp file to pandas.dataframe

```
from DSSParser import parseDSSP
parser = parseDSSP('2GW9.dssp')
parser.parse()
pddict = parser.dictTodataframe()
```

Transform between the PDB format and dssp format

```
from DSSPparser import pdbToxssp
result = pdbToxssp("2GW9")
```

## License

Released under the MIT license.
