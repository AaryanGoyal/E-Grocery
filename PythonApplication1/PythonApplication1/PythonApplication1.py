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

def signup():
    number=number_var.get()
    password=password_var.get()
    type=type_var.get()
    print(number,password,type)
    
    query="""INSERT INTO LoginData (Number,Password,Type) 
                         VALUES (%s,%s,%s)"""
    args=(number,password,type)
    execute_query(mydb,query,args)
    return

signuppage=Tk()  
signuppage.geometry('400x150')  
signuppage.title('Tkinter Signup Form - Details')

numberLabel = Label(signuppage, text="Number").grid(row=0, column=0)
number_var= StringVar()
numberEntry = Entry(signuppage, textvariable=number_var).grid(row=0, column=1)

passwordLabel = Label(signuppage,text="Password").grid(row=1, column=0)  
password_var= StringVar()
passwordEntry = Entry(signuppage, textvariable=password_var, show="*").grid(row=1, column=1)

type_var=StringVar()
customerButton=Radiobutton(signuppage,text="Customer",value="customer",variable=type_var).grid(row=2, column=5)
shopkeeperButton=Radiobutton(signuppage,text="Shopkeeper",value="shopkeeper",variable=type_var).grid(row=3, column=5)

signupButton = Button(signuppage, text="Sign up", command=signup).grid(row=6, column=0)

signuppage.mainloop()