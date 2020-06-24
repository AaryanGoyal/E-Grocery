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


class Welcome():

    def __init__(self,master):

        self.master=master
        self.master.geometry('400x150')  
        self.master.title('WELCOME')
        self.button1 = Button(self.master, text="Login", command=self.gotoSignup).grid(row=4, column=0)
        self.button2 = Button(self.master, text="Signup", command=self.gotoSignup).grid(row=6, column=0)

    def gotoSignup(self):
        self.master.destroy()
        root2=Toplevel(self.master)
        signup=Signup(root2)

class Signup():
    
    def __init__(self,master):

        self.master=master
        self.master.geometry('400x150')  
        self.master.title('Tkinter Signup Form - Details')

        self.numberLabel = Label(self.master, text="Number").grid(row=0, column=0)
        self.number_var= StringVar()
        self.numberEntry = Entry(self.master, textvariable=self.number_var).grid(row=0, column=1)

        self.passwordLabel = Label(self.master,text="Password").grid(row=1, column=0)  
        self.password_var= StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password_var, show="*").grid(row=1, column=1)

        self.type_var=StringVar(value="1")
        self.customerButton=Radiobutton(self.master,text="Customer",value="customer",variable=self.type_var).grid(row=2, column=5)
        self.shopkeeperButton=Radiobutton(self.master,text="Shopkeeper",value="shopkeeper",variable=self.type_var).grid(row=3, column=5)

        self.signupButton = Button(self.master, text="Sign up", command=self.signup).grid(row=6, column=3)

    def signup(self):
        number=self.number_var.get()
        password=self.password_var.get()
        type=self.type_var.get()
        print(number,password,type)
    
        query="""INSERT INTO LoginData (Number,Password,Type) 
                             VALUES (%s,%s,%s)"""
        args=(number,password,type)
        execute_query(mydb,query,args)
        return

root=Tk()
root.withdraw()
root1=Tk()
welcome=Welcome(root1)
root.mainloop()