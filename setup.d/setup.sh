#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit 1
fi

# init config file for mongodb & start mongodb
if [ -f "/vagrant/mongodb.d/$1-conf.yaml" ]; then
	cp "/vagrant/mongodb.d/$1-conf.yaml" /etc/mongod.conf
fi

# init web app
if [[ "$1" == *"web"* ]]; then
	sudo cp -r /vagrant/BookstoreApp /var/www
	sudo cp /vagrant/setup.d/bookstore-site.conf /etc/apache2/sites-available
	sudo a2ensite bookstore-site
	sudo service apache2 restart
fi

# prepare & run consul agent
cp /vagrant/bin/consul /usr/bin
[ -d /etc/consul.d ] || sudo mkdir /etc/consul.d
cp "/vagrant/consul.d/agents/$1.json" "/etc/consul.d/$1c.json"
cp "/vagrant/consul.d/services/$1-svc.conf" "/etc/consul.d/$1s.json"
