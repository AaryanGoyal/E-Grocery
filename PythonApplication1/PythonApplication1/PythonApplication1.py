from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="remotemysql.com",
    user="V2wcYPWEoG",
    password="h3zp3K7DHj",
    database="V2wcYPWEoG")
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

    number=""
    def __init__(self,master):
        self.master=master
        self.master.geometry('400x150')  
        self.master.title('WELCOME')
        self.button1 = Button(self.master, text="Login", command=self.gotoLogin).grid(row=0, column=0, sticky=CENTER )
        self.button2 = Button(self.master, text="Signup", command=self.gotoSignup).grid(row=0, column=0)

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

        self.loginButton = Button(self.master, text="Log In", command=self.login).grid(row=2, column=1)

    def login(self):
        Welcome.number=self.number_var.get()
        self.password=self.password_var.get()
        print(Welcome.number,self.password)
        
        query="""SELECT Password FROM LoginData where Number=%s"""
        args=(Welcome.number,)
        password_check=Sql(query,args)
        password_correct=password_check.cursor.fetchone()
        
        if password_correct[0]==self.password:
            print(password_correct[0],"correct")

            query="""SELECT Name,Type FROM LoginData where Number=%s"""
            args=(Welcome.number,)
            succesful_login=Sql(query,args)
            succesful_message=succesful_login.cursor.fetchall()
            print("Hello",succesful_message[0][0],"you are a",succesful_message[0][1],"its good to see you")

            if succesful_message[0][1]=="customer":
                self.gotoCustomer()
            else:
                self.gotoShopkeeper()
            
        else:
            print("wrong,try again")

    def gotoCustomer(self):
        self.master.destroy()
        root1=Toplevel()
        customer=Customer(root1)

    def gotoShopkeeper(self):
        self.master.destroy()
        root1=Toplevel()
        shopkeeper=Shopkeeper(root1)

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
        Welcome.number=self.number_var.get()
        self.password=self.password_var.get()
        self.type=self.type_var.get()
        self.name=self.name_var.get()
        print(Welcome.number,self.password,self.type,self.name)
    
        query="""INSERT INTO LoginData (Number,Password,Type,Name) VALUES (%s,%s,%s,%s)"""
        args=(Welcome.number,self.password,self.type,self.name)
        signin=Sql(query,args)
        mydb.commit()

        if self.type=="customer":
            self.gotoCustomer()
        else:
            self.gotoShopkeeper()

    def gotoCustomer(self):
        self.master.destroy()
        root1=Toplevel()
        customer=Customer(root1)

    def gotoShopkeeper(self):
        self.master.destroy()
        root1=Toplevel()
        shopkeeper=Shopkeeper(root1)
        return

class Customer():#most probably not complete check and complete 
    
    def __init__(self,master):
        self.master=master
        self.master.geometry('500x150')
        self.master.title('Customer Page')

        frame=LabelFrame(self.master, text='Place new order')
        frame.grid(row=0,column=1)

        self.itemLabel = Label(frame,text="Item").grid(row=1, column=0) 
        self.item_var= StringVar() 
        self.itemEntry = Entry(frame, textvariable=self.item_var)
        self.itemEntry.grid(row=1, column=1)
        
        self.quantityLabel = Label(frame,text="Quantity").grid(row=2, column=0)
        self.quantity_var= StringVar()          
        self.quantityEntry = Entry(frame, textvariable=self.quantity_var)
        self.quantityEntry.grid(row=2, column=1)

        self.viewOrder()
        self.orderButton = Button(frame, text="Place Order", command=self.placeOrder).grid(row=3, column=1)

    def viewOrder(self):
        self.tree=ttk.Treeview(self.master)
        self.tree.grid(row=6,column=1)
        self.scrollbar = ttk.Scrollbar(window,orient ="vertical",command = selftree.yview)

        self.tree['column']=("column1","column2","column3","column4")
        self.tree['show'] ='headings'

        self.tree.column("column1", width=100, minwidth=75)
        self.tree.column("column2", width=100, minwidth=75)
        self.tree.column("column3", width=100, minwidth=75)
        self.tree.column("column4", width=100, minwidth=75)


        self.tree.heading("column1", text="S.NO",anchor=W)
        self.tree.heading("column2", text="Order ID",anchor=W)
        self.tree.heading("column3", text="ITEM NAME",anchor=W)
        self.tree.heading("column4", text="QUANTITY",anchor=W)

        query="""SELECT * FROM OrderData WHERE Number=%s"""
        args=(Welcome.number,)
        orderdata=Sql(query,args)
        orderDataDisplay=orderdata.cursor.fetchall()
        print(orderDataDisplay)
        self.serial=0
        for i in orderDataDisplay:
            self.serial+=1
            self.tree.insert("","end",values=((self.serial),(i[0]),(i[2]),(i[3])))


    def placeOrder(self):
        self.item=self.item_var.get()
        self.quantity=self.quantity_var.get()

        print(Welcome.number,self.item,self.quantity)
        query="""INSERT INTO OrderData (Number,Item,Quantity) VALUES (%s,%s,%s)"""
        args=(Welcome.number,self.item,self.quantity)
        placeorder=Sql(query,args)
        mydb.commit()
        self.itemEntry.delete(0,'end')
        self.quantityEntry.delete(0,'end')
        self.viewOrder()


    
class Shopkeeper():
    
    number=""
    def __init__(self,master):
        self.master=master
        self.master.geometry('500x150')
        self.master.title('Customer Page')

        self.Label = Label(self.master, text="Hello Shopkeeper, These are the order:-").grid(row=0, column=0)#put name of user instead of shopkeeper

        self.vieworderbutton= Button(self.master,text="View Orders",command=self.viewOrder).grid(row=1,column=1)

        tree=ttk.Treeview(self.master)
        tree.grid(row=6,column=7)

        tree['column']=("column1","column2")
        tree['show'] ='headings'

        tree.column("column1", width=100, minwidth=75)
        tree.column("column2", width=100, minwidth=75)

        tree.heading("column1", text="ITEM",anchor=W)
        tree.heading("column2", text="QUANTITY",anchor=W)

        Row1=tree.insert("",1,text ="L1",values =(self.item,self.quantity))
    def viewOrder(self):
        query="""SELECT * FROM OrderData"""
        args=()
        orderdata=Sql(query,args)
        orderdatadisplay=orderdata.cursor.fetchall()
        print(orderdatadisplay)
        




root=Tk()
root.withdraw()
root1=Tk()
welcome=Welcome(root1)
root.mainloop()
#https://www.youtube.com/watch?v=HSyERXCiAtI

