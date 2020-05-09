#!/bin/bash

echo "Anonimize cloud server IP "

#######Install AMI dependencies for AWS-linux###########
#yum install docker
#yum install git 
#####################################################


echo Server Name :  `uname -a`
echo "Public hosts Origen Ip "`curl ifconfig.co`
mkdir -v  container
cd container

wget https://raw.githubusercontent.com/f0ns1/evilBrowser/master/Dockerfile
sudo docker build -t proxy 
sudo docker run --cap-add=NET_ADMIN  proxy  && sleep 10 && echo "Anonymous contaniner Succesfully upload "
