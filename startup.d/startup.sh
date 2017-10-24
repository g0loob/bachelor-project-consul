#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit 1
fi

sudo service mongod restart

consul agent -config-dir=/etc/consul.d > "/vagrant/output.d/$1-consul.output" 2>&1 &
