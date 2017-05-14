#!/bin/bash

# flask12.bash

# This script should run a python script which then starts a web server.

export FLASK_DEBUG=1
export PORT=5012
~/anaconda3/bin/python keras12.py

# In other shell I could run this:
# curl localhost:5012/nnmodel/IBM/2017/3/2/3?features=pctlag1,slope2,dow,moy

exit
