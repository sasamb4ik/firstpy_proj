#!/bin/bash

echo "Root permissions are required to install dependencies."

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
pip3 install -r requirements.txt
chmod +x run.sh
