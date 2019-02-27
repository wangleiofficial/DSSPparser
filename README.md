DSSPparser
======
DSSPparser is easy to parse dssp file, and can transform PDB format file to dssp format file by [xssp](http://www.cmbi.ru.nl/xssp/api/),also support the tansfrom between the PDB id and dssp format, hssp format and sequence.

Examples
--------

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

License
-------

Released under the MIT license.