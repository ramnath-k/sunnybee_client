# sunnybee_client
## Python Django client to visualize Sunnybee's tag tracker data


#### Installation
1. Install Python 3.4.4 (not the latest 3.5) using the windows installer at https://www.python.org/downloads/ 
1. Ensure to add Python to PATH (There is a check box in the installer)
1. Install MySQL 5.7 for windows. 
1. Ensure to install the connector for Python 3.4 x64
1. Open command prompt in windows and execute the following commands
1. `python -m pip install -U pip`
1. `python -m pip install virtualenvwrapper-win`
1. `mkvirtualenv sunnybee`
1. `workon sunnybee`
1. `python -m pip install django==1.8.13`
1. Install git for windows. In the installer enable two factor auth but leave other settings as is.
1. git clone this repository
1. from the command line execute `python manage.py runserver` to start the webserver
1. go to http://localhost:8000/<endpoint> to view your webserver
1. <endpoints> are defined in urls.py in this repository
