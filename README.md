# Reto-Squadmakers
# Getting Started

* Create a database in Mysql or MariaDB

* Create a file called .env based on .env.example

* Configurate credentials in .env

### Install virtual environment

Unix Bash (Linux, Mac, etc.):
```sh
$ pip3 install virtualenv
```
Windows:
```sh
$ pip install virtualenv
```
### Create virtual environment
Unix Bash (Linux, Mac, etc.):
```sh
$ python3 -m venv venv
```
Windows:
```sh
virtualenv venv
```
### Activate virtual enviroment

Unix Bash (Linux, Mac, etc.):
```sh
$ chmod +x ./venv/bin/activate
```
```sh
$ ./venv/bin/activate 
```
Windows:
```sh
$ .\venv\Scripts\activate.bat
```
### Install the dependencies:
```sh
$ pip install -r packages.txt
```

#### Init database:

```sh
$ flask init-db
```

### Run in dev mode:

Unix Bash (Linux, Mac, etc.):
```sh
$ export FLASK_APP=app 
$ export FLASK_ENV=development
$ flask run
```
Windows CMD:
```sh
$ set FLASK_APP=app
$ set FLASK_ENV=development
$ flask run
```
Windows PowerShell:
```sh
$ $env:FLASK_APP = "app"
$ $env:FLASK_ENV = "development"
$ flask run
```

### Built With
- Python 3
- Mysql
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
