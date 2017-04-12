# Dockerizing MongoDB: Dockerfile for building MongoDB images
# Based on ubuntu:latest, installs MongoDB folling the instruction from :
# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

FROM ubuntu:latest

# Installation
# Import MonboDB public GPG key AND create a MongoDB list files

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mogodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f 2)/mongodb-org/3.2 multiverse | tee /etc/apt/sources.list.d/mongodb-org-3.2.list"

# Update apt-get source and install MongoDB
#RUN apt-get update && apt-get install -y mongodb-org
RUN apt-get update
RUN apt-get install -y mongodb mongodb-clients mongodb-server

# Create the MongoDB data directory
RUN mkdir -p /data/db

# Expose port 27018 from the container to the host
EXPOSE 27017

# Set user/bin/mongod as the dockerized entry-point application
ENTRYPOINT ["/usr/bin/mongod"]
