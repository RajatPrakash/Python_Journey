from password import password
import mysql.connector
import re

conn = mysql.connector.connect(host="localhost",db="rajat",user="root",password="9711289764")
count = 0
if conn.is_connected():
    cursor = conn.cursor()
    first_name = input("Enter your name: ")
    password = input("Enter password: ")
    # password(password)
    sql = "select * from login "
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        #print(row[0],row[2])
        if row[0] == first_name and row[2] == password:
           print("Match found")
           break

