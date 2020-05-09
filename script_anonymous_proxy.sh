#!/bin/bash


IP_ORIGIN_LOCAL=`ifconfig -a | grep -A1 eth0 | grep inet`
SERVER_NAME=`uname -a`

PUBLIC_IP=`curl https://ipinfo.io/ip`
PUBLIC_GEO_LOCATION=`curl https://ipvigilante.com/$PUBLIC_IP`
anonsurf status
anonsurf start
ANONYMOUS_IP=`curl https://ipinfo.io/ip`
ANONYMOUS_GEO_LOCATION=`curl https://ipvigilante.com/$ANONYMOUS_IP`

echo "....................SERVER ............................."
echo ".." $SERVER_NAME
echo "-- LOCAL NETWORK -- "$IP_ORIGIN_LOCAL
echo ""
echo " PUBLIC_IP = $PUBLIC_IP"
echo " PUBLIC_GEO_LOCATION =  $PUBLIC_GEO_LOCATION"
echo "---------------------------------------------------------"
echo " Anonymous  location : "
echo  $ANONYMOUS_IP
echo " GEO LOCATION = " $ANONYMOUS_GEO_LOCATION
echo -----------------------------------------------------------
