import mysql.connector

conn = mysql.connector.connect(username='root', password='Umer@123',host='localhost',database='face_recog')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()