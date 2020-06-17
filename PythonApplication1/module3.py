import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="dIDu0XCFUx",
  password="0b0tyuI5rw",
  database="dIDu0XCFUx")


print(mydb)
cursor=mydb.cursor()
cursor.execute(
                INSERT INTO Details ("Name","Number") 
                VALUES 
                ("aaryan","number")
                )
mydb.commit()
