# README.md

This repo is discussed in my class:

http://ml4.us/cclasses/class10

This repo is a mix of technology to help end-users forecast the stock market closing price tomorrow:

  * Anaconda Python 4.2.0
  * Keras
  * SQLAlchemy
  * Flask-RESTful
  * Postgres 9.5

I intend for this repo to be deployed to a VirtualBox instance running Ubuntu 16.04.

I offer two types of instructions:

  * Simple Instructions
  * Detailed Instructions

I suggest that you follow the Simple Instructions.

# Simple Instructions

  * Install VirtualBox on your laptop
  * Import this VirtualBox Appliance:
  * https://drive.google.com/file/d/0Bx3iDDAtxxI4U3oycjR0RXpJblU
  * Above Appliance is 8.1 GB
  * Start the appliance and login as ann, passwd: a
  * Clone the keras11 repo with this shell syntax:
```bash
cd ~
rm -rf keras11
git clone https://github.com/danbikle/keras11
```
  * Run the first demo with a simple shell command:
```bash
cd ~/keras11
python import_keras11.py
```

