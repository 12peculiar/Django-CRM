#Install Mysql on your computer
#
#pip install mysql
#pip install mysql connector
#pip install mysql-connector-python

import mysql
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute('CREATE DATABASE syst')

print("ALL DONE!")

