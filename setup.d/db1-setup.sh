#!/usr/bin/env bash

echo "Waiting for consul to start..."
sleep 5
# init replica set
echo `cat /vagrant/mongodb.d/rs-conf.json` | \
	{ read conf; mongo --host 172.28.128.4 --eval "rs.initiate($conf)"; }

echo "Waiting for mongodb to set up..."
sleep 10
# init db with bookstore docs
mongoimport --host=172.28.128.4 --db bookstore --collection books \
	--drop --file /vagrant/mongodb.d/catalog-books.json
