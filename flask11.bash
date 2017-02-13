#!/bin/bash

# flask11.bash

# This script should run a python script which then starts a web server.

export FLASK_DEBUG=1
export PORT=5011
~/anaconda3/bin/python keras11.py

# In other shell I could run this:
# bash -x curlem.bash

exit
