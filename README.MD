# Installations
> download python 
- [python 3.6 +](https://python.org)
- browse how to install python properly

## INSTALL POSTGRESS & REQUIREMENTS UBUNTU
>##### sudo apt-get update
>##### sudo apt-get install python3-pip python-dev libpq-dev virtualenv
>##### sudo apt-get install wget ca-certificates
>##### sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
>##### sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
>##### sudo apt-get update
>##### sudo apt-get install postgresql postgresql-contrib
## INSTALL POSTGRESS & REQUIREMENTS WINDOWS
### install postgress
[tutorial](https://www.postgresqltutorial.com/install-postgresql/)
### Download Python 3.6+ 
[link](https://www.python.org/downloads/)

# CREATE DATABASE UBUNTU & WINDOWS
##### Create a Database and Database User
By default, Postgres uses an authentication scheme called “peer authentication” for local connections. Basically, this means that if the user’s operating system username matches a valid Postgres username, that user can login with no further authentication.

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to change to this user to perform administrative tasks:
## For Ubuntu
>#### ```sudo su - postgres```
You should now be in a shell session for the postgres user. Log into a Postgres session by typing:
## For Windows
[![N|Solid](https://sp.postgresqltutorial.com/wp-content/uploads/2019/05/Install-PostgreSQL-psql.png)](https://www.postgresqltutorial.com/install-postgresql/)

## Preparing to run the project
Once you have all installed the setup, now please go inside the porject and make migration, then start the python server by using below command:
```python manage.py makemigrations````
```python manage.py migrate````
```pyhton manange.py runserver```
From there you can hit this url to retrive data "localhost:8000/api_test/lists"