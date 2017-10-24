# Consul as a solution for service discovery problem in microservices architecture

## Overview

This project represents practical part of my bachelor thesis. It uses *Vagrant* to create 4 VMs (nodes) which will form *Consul* cluster. Because it's all about **microservices architecture**, two nodes have *web service* (web application) and two nodes have *database service*. You can access this system locally from your browser visiting `bookstore.sg`, but more information will be provided in the next section. The Web application is a simple bookstore app that allows you to go through a collection of books.

## Exploring everything locally

You can play with *Consul* and microservices locally:
```
git clone https://github.com/g0loob/bachelor-project-consul.git
cd bachelor-project-consul
vagrant up
```
and wait for everything to set up. It can take approximately 20-30 min (depending on your internet connection). Setup consists of:

- downloading `Ubuntu 16.04` box if you haven't installed it previously
- updating packages installed on VM
- installing `MongoDB`
- installing `apache2`, `mod_wsgi`, `pip`, `virtualenv`, `Flask`, `pymongo`, `request`, `py2-ipaddress` on web nodes
- setting up web application on web nodes
- copying configuration files for web server, db and Consul agents
- starting Consul agents

Because the network set up with *Vagrant* is private, you can't pass DNS queries from browser to Consul machines, so in order to use web application from browser you'll have to add following lines to `/etc/hosts` file on your host machine:
```
172.28.128.3	bookstore.sg
172.28.128.6	bookstore.sg
```

When you do that, and everything is set up, you can start exploring. You can access the web application from browser by going to `bookstore.sg` and Consul Web UI is available on `bookstore.sg:8500/ui`. 


## Project details

### Vagrant 

The core of the project is `Vagrant` v1.9.8. Every VM uses `bento/ubuntu-16.04` box. 

### Consul

The heart of the project is `Consul` v0.9.3 which you can find on every node. Consul setup/binary is located in `bin` directory of the project. To use Consul, you need to configure it. All files needed to set up Consul agents are in `consul.d` directory. In this directory you'll find two directory `agents` and `services`. 

`agents` directory contains configuration files for Consul agents, while `services` directory contains configuration files for services that nodes in this system provide. For monitoring what Consul does in background you can access output files in `output.d` directory.

### Web application

When Consul agents are set up, next thing we need are services that Consul agents claim that we have. Web service or web application is located in `BookstoreApp` directory. This directory contains the web app (in `Bookstore` directory) and WSGI script needed when deploying app on Apache server. Key components of web app are:

- `Flask` v0.12.2 with `Python` 2.7
- `PyMongo` v3.5.1 driver for communication with MongoDB databases
- `requests` v2.18.4 for accessing Consul HTTP API
- `py2-ipaddress` for finding server's IP address on which web app runs

### MongoDB

For web app to work properly, it needs information from databases so that it can present them. Database used in this project is `MongoDB` v3.4.9. Configuration files for databases are located in `mongodb.d` directory. In this directory there is also JSON file containing documents that represent books for bookstore app. 

MongoDB replica set is used for replicating bookstore database between two db nodes, and extra node (web1 node) is used as an arbiter node if one of the db nodes goes down.

### Other

Because the idea was to automate everything in this project, there are some shell scripts helping out and are located in `vmsetup.d`, `setup.d` and `startup.d` directories. In `setup.d`, you can also find configuration file for creating virtual host on Apache server when deploying web app.
