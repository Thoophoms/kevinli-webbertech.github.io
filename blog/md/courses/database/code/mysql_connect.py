import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mysql')
mycursor = mydb.cursor()

mycursor.execute("select * from user")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mydb.close()