#!/usr/bin/env bash

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get install -y mongodb-org

if [[ "$1" == *"web"* ]]; then
	sudo apt-get install -y apache2 libapache2-mod-wsgi python-dev

	sudo a2enmod wsgi 

	sudo apt-get install -y python-pip 
	sudo pip install --upgrade pip

	sudo pip install virtualenv

	sudo pip install Flask==0.12.2
	sudo pip install requests==2.18.4
	sudo pip install pymongo==3.5.1
	sudo pip install py2-ipaddress
fi
