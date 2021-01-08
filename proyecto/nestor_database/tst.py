import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="nestormsj"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mensajes (texto) VALUES %s"
val = 'tengo hambre'
#mycursor.execute(sql, (val,))
mycursor.execute("INSERT INTO mensajes (texto) VALUES ('prueba')")

mydb.commit()

print(mycursor.rowcount, "record inserted.")