from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="dIDu0XCFUx",
  password="0b0tyuI5rw",
  database="dIDu0XCFUx")

print(mydb)

def execute_query(connection,query,args):
    cursor = connection.cursor()
    try:
        cursor.execute(query,args)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        return

def Login():
    name=name_var.get()
    number=number_var.get()
    print(name,number)
    
    query="""INSERT INTO testing (Name,Number) 
                         VALUES (%s,%s)"""
    args=(name,number)
    execute_query(mydb,query,args)
    return

loginpage=Tk()  
loginpage.geometry('400x150')  
loginpage.title('Tkinter Login Form - Details')

nameLabel = Label(loginpage, text="Name").grid(row=0, column=0)
name_var= StringVar()
nameEntry = Entry(loginpage, textvariable=name_var).grid(row=0, column=1)

numberLabel = Label(loginpage,text="Phone Number").grid(row=1, column=0)  
number_var= StringVar()
numberEntry = Entry(loginpage, textvariable=number_var).grid(row=1, column=1)

loginButton = Button(loginpage, text="Login", command=Login).grid(row=4, column=0)

loginpage.mainloop()