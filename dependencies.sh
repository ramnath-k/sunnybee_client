#!/bin/bash
sudo apt-get install git
git clone https://github.com/ramnath-k/sunnybee_client.git
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv sunnybee
workon sunnybee
pip install -r requirements.txt

