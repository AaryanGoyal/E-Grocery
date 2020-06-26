from tkinter import *
import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="remotemysql.com",
    user="dIDu0XCFUx",
    password="0b0tyuI5rw",
    database="dIDu0XCFUx")

print(mydb)

class Sql():

    def __init__(self,query,args):
        self.cursor=mydb.cursor()
        try:
            self.cursor.execute(query,args)
            print("Query executed successfully")
        except Error as e:
            print("The error '{e}' occurred")
            return


class Welcome():

    def __init__(self,master):
        self.master=master
        self.master.geometry('400x150')  
        self.master.title('WELCOME')
        self.button1 = Button(self.master, text="Login", command=self.gotoLogin).grid(row=4, column=0)
        self.button2 = Button(self.master, text="Signup", command=self.gotoSignup).grid(row=6, column=0)

    def gotoSignup(self):
        self.master.destroy()
        root1=Toplevel()
        signup=Signup(root1)

    def gotoLogin(self):
        self.master.destroy()
        root1=Toplevel()
        login=Login(root1)


class Login():

    def __init__(self,master):
        self.master=master
        self.master.geometry('400x150')  
        self.master.title('Login Page')

        self.numberLabel = Label(self.master, text="Number").grid(row=0, column=0)
        self.number_var= StringVar()
        self.numberEntry = Entry(self.master, textvariable=self.number_var).grid(row=0, column=1)

        self.passwordLabel = Label(self.master,text="Password").grid(row=1, column=0)  
        self.password_var= StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password_var, show="*").grid(row=1, column=1)

        self.loginButton = Button(self.master, text="Log In", command=self.login).grid(row=6, column=3)

    def login(self):
        self.number=self.number_var.get()
        self.password=self.password_var.get()
        print(self.number,self.password)
        
        query="""SELECT Password FROM LoginData where Number=%s"""
        args=(self.number,)
        password_check=Sql(query,args)
        password1=password_check.cursor.fetchone()
       
        if password1[0]==self.password:
            print(password1[0],"correct")
            query="""SELECT Name,Type FROM LoginData where Number=%s"""
            args=(self.number,)
            succesful_login=Sql(query,args)
            succesful_message=succesful_login.cursor.fetchall()
            print("Hello",succesful_message[0][0],"you are a",succesful_message[0][1],"its good to see you")
            
        else:
            print("wrong")

class Signup():
    
    def __init__(self,master):

        self.master=master
        self.master.geometry('400x150')  
        self.master.title('Signup Page')

        self.numberLabel = Label(self.master, text="Number").grid(row=0, column=0)
        self.number_var= StringVar()
        self.numberEntry = Entry(self.master, textvariable=self.number_var).grid(row=0, column=1)

        self.passwordLabel = Label(self.master,text="Password").grid(row=1, column=0)  
        self.password_var= StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password_var, show="*").grid(row=1, column=1)

        self.nameLabel = Label(self.master,text="Name").grid(row=2, column=0)  
        self.name_var= StringVar()
        self.nameEntry = Entry(self.master, textvariable=self.name_var).grid(row=2, column=1)

        self.type_var=StringVar(value="1")
        self.customerButton=Radiobutton(self.master,text="Customer",value="customer",variable=self.type_var).grid(row=3, column=5)
        self.shopkeeperButton=Radiobutton(self.master,text="Shopkeeper",value="shopkeeper",variable=self.type_var).grid(row=4, column=5)

        self.signupButton = Button(self.master, text="Sign up", command=self.signup).grid(row=6, column=3)

    def signup(self):
        self.number=self.number_var.get()
        self.password=self.password_var.get()
        self.type=self.type_var.get()
        self.name=self.name_var.get()
        print(self.number,self.password,self.type,self.name)
    
        query="""INSERT INTO LoginData (Number,Password,Type,Name) 
                             VALUES (%s,%s,%s,%s)"""
        args=(self.number,self.password,self.type,self.name)
        signin=Sql(query,args)
        mydb.commit()
        return


root=Tk()
root.withdraw()
root1=Tk()
welcome=Welcome(root1)
root.mainloop()

#testin vscode
#hello kay2
#hello Head boi
