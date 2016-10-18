#!/bin/bash
DISTRIBUTION=$(lsb_release -c -s)
echo $DISTRIBUTION
if [[ ! "trusty wily xenial yakkety" == *"$DISTRIBUTION"*  ]]; then
	echo "only Ubuntu trusty, wily, xenial, yakkety are supported"
else
	echo "Installing for Ubuntu $DISTRIBUTION"
fi

FILE="/etc/apt/sources.list"

L1="deb http://downloads.skewed.de/apt/$DISTRIBUTION $DISTRIBUTION universe"
L2="deb-src http://downloads.skewed.de/apt/$DISTRIBUTION $DISTRIBUTION universe"

if [ -z "$(grep "$L1" "$FILE")" ]; then 
	echo $L1 >> $FILE
	echo $L2 >> $FILE
fi

if [ "$1" == "python3" ]; 
then
	echo "Installing for graph-tool python3"
	sudo apt-get install python3-graph-tool;
else
	echo "Installing for graph-tool python2"
	sudo apt-get install python-graph-tool;
fi
