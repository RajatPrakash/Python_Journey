import mysql.connector

conn = mysql.connector.connect(host="localhost",db="rajat",user="root",password="9711289764")

if conn.is_connected():
    print("You are in...")
cursor = conn.cursor()
while(True):
    query = input("INSERT / SELECT.... ").upper()
    if query == 'INSERT':
        script = """insert into login(first_name,last_name,password) values(%s,%s,%s)"""
        user_input = (input('enter the first name'),input('enter the last name'),input('enter the password'))
        try:
            cursor.execute(script,user_input)
            conn.commit()
            print("record inserted sucessfully")
        except:
            conn.rollback()
            print("trasaction is rolled backed ")
    elif query == 'SELECT':
        cursor.execute("select * from login")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        break
    else:
        print("Type either insert or select")
cursor.close()
conn.close()



