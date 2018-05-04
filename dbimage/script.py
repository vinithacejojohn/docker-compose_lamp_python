#!/usr/bin/python3.4

# Connect to the database.
import pymysql

# Open database connection
db = pymysql.connect("localhost","root","testpass")

# prepare a cursor object using cursor() method
c = db.cursor()

c.execute("GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'testpass' WITH GRANT OPTION")
c.execute("FLUSH PRIVILEGES")

# disconnect from server
db.close()

