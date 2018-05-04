#!/usr/bin/python3.5

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html\n")
print()

# Connect to the database.
import pymysql

# Open database connection
db = pymysql.connect("db","test","testpass")

# prepare a cursor object using cursor() method
c = db.cursor()

#sql = 'CREATE DATABASE TESTDB'
#c.execute(sql)
# disconnect from server
#db.close()

db = pymysql.connect("db","test","testpass","testdb")

# prepare a cursor object using cursor() method
c = db.cursor()

c.execute("CREATE TABLE names( Number INT, Names CHAR(10))")
# Insert some example data.
c.execute("INSERT INTO names VALUES (1, 'Vinitha!')")
c.execute("INSERT INTO names VALUES (2, 'Cejo!')")
c.execute("INSERT INTO names VALUES (3, 'John!')")

# Print the contents of the database.
c.execute("SELECT * FROM names")
print([(r[0], r[1]) for r in c.fetchall()])

# disconnect from server
db.close()

