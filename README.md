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
  * https://drive.google.com/file/d/10p1W7kqzxE69jODhUzcb-qi-osN4htO-
  * Above Appliance is 13 GB
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

  * The above demo shows how to access the keras11-API using Python.
  * The demo below shows how to access the keras11-API using HTTP-GET.

  * Run the next demo with a simple shell command:
```bash
cd ~/keras11
./flask11.bash
```

  * The above shell is running a webserver. You should leave it alone.
  * The next demo requires another shell. So, start another shell.
  * Run the next demo with a simple shell command:
```bash
cd ~/keras11
bash -x curlem.bash
```


# Detailed Instructions

  * These instructions assume that you have Linux training
  * Also you should know how to interact with a shell in a terminal
  * If Linux and shell are new to you, you will need some training before going further
  * Here are paths toward free training:
  * http://www.google.com/search?q=Simple+Linux+Tutorial
  * http://www.google.com/search?q=Simple+Shell+Tutorial
  * http://www.google.com/search?tbm=vid&q=Simple+Linux+Tutorial
  * http://www.google.com/search?tbm=vid&q=Simple+Shell+Tutorial
  * The detailed instructions below, assume that you have a laptop which can run VirtualBox
  * You can get VirtualBox from this URL:
  * https://www.virtualbox.org/wiki/Downloads
  * After you install VirtualBox, you should install Ubuntu16 inside of VirtualBox
  * Ubuntu16 is at this URL:
  * http://releases.ubuntu.com/xenial/ubuntu-16.04.1-desktop-amd64.iso
  * If you need help installing Ubuntu16 inside of VirtualBox, the links below might be helpful
  * http://www.google.com/search?q=how+to+install+ubuntu16+inside+VirtualBox
  * http://www.google.com/search?tbm=vid&q=how+to+install+ubuntu16+inside+VirtualBox
  * After you install Ubuntu16, you should install an account named 'ann'
  * Shell commands to install the ann account are listed below:
```bash
sudo useradd -m -s /bin/bash -G sudo ann
sudo passwd ann
```
  * Next login as ann
  * Next, you should enhance your copy of Ubuntu 16:
```bash
sudo apt-get install autoconf bison build-essential libssl-dev libyaml-dev    \
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 curl          \
libgdbm-dev libsqlite3-dev gitk postgresql postgresql-server-dev-all aptitude \
libpq-dev emacs wget openssh-server libbz2-dev linux-headers-$(uname -r)
```
  * After the above command finishes, you should reboot Ubuntu16
  * Next you should create a role inside of Postgres named ann which has password: ann
  * The commands below do that:
```bash
sudo su - postgres
```
  * Now, you should be inside the postgres Linux account:
```bash
psql
```
  * Now, you should be inside the postgres Database account
```sql
CREATE ROLE ANN WITH LOGIN SUPERUSER PASSWORD 'ann';
CREATE DATABASE ann;
```
  * Now, here is the tricky part. Many students fail here.
  * Exit the Database account:
```sql
\q
```
  * Exit the postgres Linux account:
```bash
exit
```
  * Ensure that you are in the ann Linux account:
```bash
id
```
  * At this point you have a role inside of Postgres named ann which has password: ann

  * Next, run these shell commands to install Anaconda:
```bash
id
cd ~ann
rm -f Anaconda3-4.2.0-Linux-x86_64.sh
rm -rf anaconda anaconda3
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh
mv anaconda3/bin/curl anaconda3/bin/curl_ana
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash
```
  * The syntax above is designed to behave well if you run it multiple times
  * This means that if you run the above syntax 4 times, you should end up with Anaconda installed
  * Next, install some packages into Anaconda:
```bash
conda install -c conda-forge flask-restful
```
  * Next, install more packages into Anaconda:
```bash
conda install psycopg2 sqlalchemy keras
```

  * Next, Clone the keras11 repo with this shell syntax:
```bash
cd ~
git clone https://github.com/danbikle/keras11
```
  * Then, Run the first demo with a simple shell command:
```bash
cd ~/keras11
python import_keras11.py
```

  * The above demo shows how to access the keras11-API using Python.
  * The demo below shows how to access the keras11-API using HTTP-GET.

  * Run the next demo with a simple shell command:
```bash
cd ~/keras11
./flask11.bash
```

  * The above shell is running a webserver. You should leave it alone.
  * The next demo requires another shell. So, start another shell.
  * Run the next demo with a simple shell command:
```bash
cd ~/keras11
bash -x curlem.bash
```
