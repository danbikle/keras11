#!/bin/bash

curl localhost:5011/skservice/SPY/2016/25
curl localhost:5011/keras/SPY/2016/25?features=pctlag1,pctlag2,slope2,slope4,dow,moy
curl localhost:5011/db/SPY/2016/25?features=pctlag1,pctlag2,slope2,slope4,dow,moy
curl localhost:5011/dbkeras/SPY/2016/25?features=pctlag1,pctlag2,slope2,slope4,dow,moy
