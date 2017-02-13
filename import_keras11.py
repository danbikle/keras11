# import_keras11.py

# This script shows how to import keras11.py.
# Then it accesses methods using Python rather than from Flask.

# Demo:
# python import_keras11.py

import sys
import keras11


s10 = keras11.SKService()
oput = s10.get(tkr='SPY', yr2predict='2016', yrs2train=25)
#print(oput)

s11 = keras11.KerasService()
oput = s11.get(local=True, tkr='SPY', yr2predict='2016', yrs2train=25, features='pctlag1,slope2,moy')
#print(oput)

s12 = keras11.DBService()
oput = s12.get(local=True, tkr='SPY', yr2predict='2016', yrs2train=25, features='pctlag1,slope2,moy')
#print(oput)

s13 = keras11.DBKerasService()
oput = s13.get(local=True, tkr='SPY', yr2predict='2008', yrs2train=24, features='pctlag1,slope2,dow,moy')
print(oput)
