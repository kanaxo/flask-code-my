# User Example App

This app is built using flask and JJinja.

It is made using codemy's Youtube Flask Fridays playlist. [Youtube](https://www.youtube.com/playlist?list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz)

## To run

Activate virtual environment.

`pip install -r requirements.txt`
Note: Create virtual environment first before installing dependencies.

`python hello.py` to run website.

## Templates

All html files are saved in templates directory.

## Database

- Run `python createdb.py` to create database
- Database is defined in `hello.py` using db.Models() using SQLAlchemy.
- If want to create MYSQL database, open up MYSQL database & Apache using **XAMPP** first before running `mysql_createdb.py` (Uncomment CREATE DATABASE) then `createdb.py`. You can click on `admin` button in XAMPP to open up PHPMyAdmin.

* Database is saved as `users.db` for SQLite
