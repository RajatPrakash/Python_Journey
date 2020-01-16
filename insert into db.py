import mysql.connector

conn = mysql.connector.connect(host="localhost",db="rajat",user="root",password="9711289764")

if conn.is_connected():
    print("you are in")

cursor = conn.cursor()
query = """insert into python (id,name) values(%s, %s)"""
val = (input("enter id: "),input('enter name'))

try:
    cursor.execute(query,val)
    conn.commit()
    print("record inserted")
    cursor.execute("select * from python")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except:
    conn.rollback()
    print("due to error transaction has been roll backed")




cursor.close()
conn.close()