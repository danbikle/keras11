# import_keras12.py

# This script shows how to import keras12.py.
# Then it accesses methods using Python rather than from Flask.

# Demo:
# python import_keras12.py

import sys
import keras12

s10 = keras12.Nnmodel()
oput = s10.get(local=True, tkr='SPY',yr2predict='2017',yrs2train=10,hlayers=1,neurons=4,features='pctlag1,slope2,moy')
print(oput)
