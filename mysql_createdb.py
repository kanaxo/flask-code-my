# pip install mysql-connector 
# mysql-connector-python mysql-connector-python-rf optional
# pip install pymysql cryptography
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "",
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# run this file
# then run createdb.py