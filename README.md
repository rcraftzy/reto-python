# Reto-Squadmakers
# Getting Started

* Create a database in Mysql or MariaDB

* Create a file called .env based on .env.example

* Configurate credentials in .env

Install the dependencies:
```sh
$ pip install -r packages.txt
```
Export app:
```sh
$ export FLASK_APP=app 
```
Init database:
```sh
$ flask init-db
```

Run in dev mode:

```sh
$ export FLASK_ENV=development
$ flask run
```

### Built With
- Python
- Mysql
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Request](https://docs.python-requests.org/en/latest/)
