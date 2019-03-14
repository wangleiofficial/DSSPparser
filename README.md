# DSSPparser

[![PyPI - Version](https://img.shields.io/pypi/v/DSSPparser.svg?style=flat)](https://pypi.org/project/DSSPparser/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DSSPparser.svg)](https://pypi.org/project/DSSPparser/)
[![GitHub - LICENSE](https://img.shields.io/github/license/neolei/DSSPparser.svg?style=flat)](./LICENSE)

DSSPparser is easy to parse dssp file, and can transform PDB format file to dssp format file by [xssp](http://www.cmbi.ru.nl/xssp/api/),also support the tansfrom between the PDB id and dssp format, hssp format and sequence.

## Examples

parse dssp file to pandas.dataframe

```Python
from DSSParser import parser
parse_ = parseDSSP('2GW9.dssp')
parse_.parse()
pddict = parse_.dictTodataframe()
```

Transform between the PDB format and dssp format

```Python
from DSSPparser import pdbToxssp
result = pdbToxssp("2GW9")
```

## License

Released under the MIT license.