#!/bin/bash
DISTRIBUTION=$(lsb_release -c -s)
echo $DISTRIBUTION
if [[ ! "trusty wily xenial yakkety" == *"$DISTRIBUTION"*  ]]; then
	echo "only Ubuntu trusty, wily, xenial, yakkety are supported"
else
	echo "Installing for Ubuntu $DISTRIBUTION"
fi
if [[ "$DISTRIBUTION" == "trusty" ]]; then
    sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test;
fi
FILE="/etc/apt/sources.list"

L1="deb http://downloads.skewed.de/apt/$DISTRIBUTION $DISTRIBUTION universe"
L2="deb-src http://downloads.skewed.de/apt/$DISTRIBUTION $DISTRIBUTION universe"

if [ -z "$(grep "$L1" "$FILE")" ]; then 
	echo $L1 >> $FILE
	echo $L2 >> $FILE
fi

sudo apt-get update;
if [ "$1" == "python3" ]; 
then
	echo "Installing for graph-tool python3"
	sudo apt-get install -y --force-yes python3-graph-tool;
else
	echo "Installing for graph-tool python2"
	sudo apt-get install -y --force-yes python-graph-tool;
fi