from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import mysql.connector
import matplotlib.pyplot as plt
from mysql.connector import Error
from PIL import ImageTk,Image 
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
    name=""
    def __init__(self,master):
        self.master=master
        self.master.geometry('250x150')  
        self.master.title('WELCOME')
        self.button1 = Button(self.master, text="Login", command=self.gotoLogin, width=15).grid(row=1, column=1, pady=6, padx=(5,4))
        self.button2 = Button(self.master, text="Signup", command=self.gotoSignup, width=15).grid(row=1, column=0, pady=6, padx=(5,4))
    
        self.image1 = Image.open("Pngtreered_shopping_bags_315306.png")
        self.resize_image=self.image1.resize((100,100))
        self.image2 = ImageTk.PhotoImage(self.resize_image)
        
        self.img=Label(self.master, image=self.image2)
        self.img.image=self.image2
        self.img.grid(row=0, column=0, columnspan=2,padx=5,pady=5)
        
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                print("SQL Connected=",mydb.is_connected())
                mydb.close()
                print("SQL Connected=",mydb.is_connected())
                print("Exiting")
                root1.destroy()
                root.destroy()
        self.master.protocol("WM_DELETE_WINDOW", on_closing)


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
        self.master.geometry('220x225')  
        self.master.title('Login')

        self.numberLabel = Label(self.master, text="Number").grid(row=1, column=0 ,pady=5, padx=4,sticky='w')
        self.number_var= StringVar()
        self.numberEntry = Entry(self.master, textvariable=self.number_var).grid(row=1, column=1 )

        self.passwordLabel = Label(self.master,text="Password").grid(row=2, column=0, sticky='w',pady=5, padx=4)  
        self.password_var= StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password_var, show="*").grid(row=2, column=1)

        self.loginButton = Button(self.master, text="Log In", command=self.login, width=15).grid(row=3, column=1, pady=5)

        self.image1 = Image.open("—Pngtree—user login or authenticate icon_5089976.png")
        self.resize_image=self.image1.resize((100,100))
        self.image2 = ImageTk.PhotoImage(self.resize_image)
        
        self.img=Label(self.master, image=self.image2)
        self.img.image=self.image2
        self.img.grid(row=0, column=1,padx=5,pady=5)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                print("SQL Connected=",mydb.is_connected())
                mydb.close()
                print("SQL Connected=",mydb.is_connected())
                print("Exiting")
                root.destroy()
        self.master.protocol("WM_DELETE_WINDOW", on_closing)

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
            Welcome.name=succesful_message[0][0]
            
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
        self.master.geometry('215x290')  
        self.master.title('Signup')

        self.numberLabel = Label(self.master, text="Number").grid(row=1, column=0,sticky='w',pady=5, padx=4)
        self.number_var= StringVar()
        self.numberEntry = Entry(self.master, textvariable=self.number_var).grid(row=1, column=1,sticky='w')

        self.passwordLabel = Label(self.master,text="Password").grid(row=2, column=0,sticky='w',pady=5, padx=4)  
        self.password_var= StringVar()
        self.passwordEntry = Entry(self.master, textvariable=self.password_var, show="*").grid(row=2, column=1,sticky='w')

        self.nameLabel = Label(self.master,text="Name").grid(row=3, column=0,sticky='w',pady=5, padx=4)  
        self.name_var= StringVar()
        self.nameEntry = Entry(self.master, textvariable=self.name_var).grid(row=3, column=1,sticky='w')

        self.type_var=StringVar(value="1")
        self.customerButton=Radiobutton(self.master,text="Customer",value="customer",variable=self.type_var).grid(row=4, column=1,sticky='w')
        self.shopkeeperButton=Radiobutton(self.master,text="Shopkeeper",value="shopkeeper",variable=self.type_var).grid(row=5, column=1,sticky='w')

        self.signupButton = Button(self.master, text="Sign up", command=self.signup, width=15).grid(row=6, column=1)

        self.image1 = Image.open("—Pngtree—user login or authenticate icon_5089976.png")
        self.resize_image=self.image1.resize((100,100))
        self.image2 = ImageTk.PhotoImage(self.resize_image)
        
        self.img=Label(self.master, image=self.image2)
        self.img.image=self.image2
        self.img.grid(row=0, column=1,padx=5,pady=5)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                print("SQL Connected=",mydb.is_connected())
                mydb.close()
                print("SQL Connected=",mydb.is_connected())
                print("Exiting")
                root.destroy()
        self.master.protocol("WM_DELETE_WINDOW", on_closing)

    def signup(self):
        Welcome.number=self.number_var.get()
        self.password=self.password_var.get()
        self.type=self.type_var.get()
        self.name=self.name_var.get()
        print(Welcome.number,self.password,self.type,self.name)
        Welcome.name=self.name

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
class Customer():

    def __init__(self,master):
        self.master=master
        self.master.geometry('550x350')
        self.master.title('Localé Bazar: '+Welcome.name)

        frame=LabelFrame(self.master, text='Place new order')
        frame.grid(row=0,column=1,pady=5)

        query="""SELECT Item FROM ItemData"""
        args=()
        itemdata=Sql(query,args)
        itemDataDisplay=itemdata.cursor.fetchall()
        itemDataDisplay.insert(0,("Please Select Item",))
        print(itemDataDisplay)

        self.itemLabel = Label(frame,text="Item").grid(row=1, column=0) 
        self.itemchosen = ttk.Combobox(frame, width = 27,values=itemDataDisplay)
        self.itemchosen.grid(row = 1, column = 1)
        self.itemchosen.current(0)

        self.quantityLabel = Label(frame,text="Quantity").grid(row=2, column=0)
        self.quantity_var= StringVar()          
        self.quantityEntry = Entry(frame, textvariable=self.quantity_var,width=30)
        self.quantityEntry.grid(row=2, column=1)

        self.viewOrder()
        self.orderButton = Button(frame, text="Place Order", command=self.placeOrder,width=20).grid(row=3, column=1)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                print("SQL Connected=",mydb.is_connected())
                mydb.close()
                print("SQL Connected=",mydb.is_connected())
                print("Exiting")
                root.destroy()
        self.master.protocol("WM_DELETE_WINDOW", on_closing)

    def viewOrder(self):
        self.tree=ttk.Treeview(self.master)
        self.tree.grid(row=6,column=1,padx=20,pady=5)

        self.tree['column']=("column1","column2","column3","column4","column5")
        self.tree['show'] ='headings'

        self.tree.column("column1", width=100, minwidth=75)
        self.tree.column("column2", width=100, minwidth=75)
        self.tree.column("column3", width=100, minwidth=75)
        self.tree.column("column4", width=100, minwidth=75)
        self.tree.column("column5", width=100, minwidth=75)

        self.tree.heading("column1", text="S.NO",anchor=W)
        self.tree.heading("column2", text="Order ID",anchor=W)
        self.tree.heading("column3", text="Item Name",anchor=W)
        self.tree.heading("column4", text="Quantity",anchor=W)
        self.tree.heading("column5", text="Completed By",anchor=W)

        query="""SELECT * FROM OrderData WHERE Number=%s"""
        args=(Welcome.number,)
        orderdata=Sql(query,args)
        orderDataDisplay=orderdata.cursor.fetchall()
        print(orderDataDisplay)
        self.serial=0
        for i in orderDataDisplay:
            self.serial+=1
            self.tree.insert("","end",values=((self.serial),(i[0]),(i[2]),(i[3]),(i[4])))

    def placeOrder(self):
        self.item=self.itemchosen.get()
        self.quantity=self.quantity_var.get()

        print(Welcome.number,self.item,self.quantity)
        query="""INSERT INTO OrderData (Number,Item,Quantity,Completed) VALUES (%s,%s,%s,"Pending")"""
        args=(Welcome.number,self.item,self.quantity)
        placeorder=Sql(query,args)
        mydb.commit()
        self.itemchosen.current(0)
        self.quantityEntry.delete(0,'end')
        self.viewOrder()
class Shopkeeper():
    
    def __init__(self,master):
        self.master=master
        self.master.geometry('325x150')  
        self.master.title('Localé Bazar: '+Welcome.name)
        self.button1 = Button(self.master, text="View Orders", command=self.gotoOrder, width=20).grid(row=1, column=0, pady=6, padx=(5,4))
        self.button2 = Button(self.master, text="View Profit Summary", command=self.viewSummary, width=20).grid(row=1, column=1, pady=6, padx=(5,4))
    
        self.image1 = Image.open("unnamed.png")
        self.resize_image=self.image1.resize((100,100))
        self.image2 = ImageTk.PhotoImage(self.resize_image)
        
        self.img=Label(self.master, image=self.image2)
        self.img.image=self.image2
        self.img.grid(row=0, column=0, columnspan=2,padx=5,pady=5)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                print("SQL Connected=",mydb.is_connected())
                mydb.close()
                print("SQL Connected=",mydb.is_connected())
                print("Exiting")
                root.destroy()
        self.master.protocol("WM_DELETE_WINDOW", on_closing)
    
    def gotoOrder(self):
        root1=Toplevel()
        order=ShopView(root1)

    def viewSummary(self):
        query="""SELECT OrderData.Item,OrderData.Quantity,ItemData.Price FROM OrderData INNER JOIN ItemData ON OrderData.Item=ItemData.Item WHERE OrderData.Completed=%s"""
        args=(Welcome.name,)
        summary=Sql(query,args)
        summaryDisplayData=summary.cursor.fetchall()
        print(summaryDisplayData)
        graphDict={}
        for x in summaryDisplayData:
            graphDict[x[0]]=0

        for x in summaryDisplayData:
            graphDict[x[0]]+=int(x[1])*int(x[2])
        print(graphDict)
        
        Xaxis=[x for x in graphDict]
        Yaxis=[graphDict[x] for x in graphDict]

        fig= plt.figure()
        plt.title("Profit Summary")
        plt.bar(Xaxis,Yaxis)
        plt.xlabel("Items")
        plt.ylabel("total earnings")
        plt.show()
class ShopView():
    
    def __init__(self,master):
        self.master=master
        self.master.geometry('550x360')
        self.master.title('View Order')

        self.Label = Label(self.master, text="Hello "+Welcome.name+" these are the orders:-",font=("Arial",17)).grid(row=0, column=0 ,padx=5,pady=5)
        self.viewOrder()

        frame=LabelFrame(self.master, text='Completed Order')
        frame.grid(row=2,column=0)

        self.orderCompLabel = Label(frame,text="Enter Order ID").grid(row=0, column=0)
        self.orderComp_var= StringVar()  
        self.orderCompEntry = Entry(frame, textvariable=self.orderComp_var)
        self.orderCompEntry.grid(row=0, column=1)
        self.orderCompButton = Button(frame, text="Order Completed", command=self.OrderComp).grid(row=1, column=1)
    
    def OrderComp(self):
        self.orderComp_ID=self.orderComp_var.get()
        
        query=""" UPDATE OrderData SET Completed=%s WHERE `Order ID`=%s"""
        args=(Welcome.name,self.orderComp_ID)
        print(args)
        completeorder=Sql(query,args)
        mydb.commit()
        self.orderCompEntry.delete(0,'end')
        self.viewOrder()

    def viewOrder(self):
        self.tree=ttk.Treeview(self.master)
        self.tree.grid(row=1,column=0,padx=20,pady=5)

        self.tree['column']=("column1","column2","column3","column4","column5")
        self.tree['show'] ='headings'

        self.tree.column("column1", width=100, minwidth=75)
        self.tree.column("column2", width=100, minwidth=75)
        self.tree.column("column3", width=100, minwidth=75)
        self.tree.column("column4", width=100, minwidth=75)
        self.tree.column("column5", width=100, minwidth=75)

        self.tree.heading("column1", text="S.NO",anchor=W)
        self.tree.heading("column2", text="Order ID",anchor=W)
        self.tree.heading("column3", text="Item Name",anchor=W)
        self.tree.heading("column4", text="Quantity",anchor=W)
        self.tree.heading("column5", text="Delivery to",anchor=W)

        query="""SELECT OrderData.`Order ID`,OrderData.Item,OrderData.Quantity,LoginData.Name,LoginData.Number FROM OrderData INNER JOIN LoginData ON OrderData.Number=LoginData.Number WHERE OrderData.Completed=%s"""
        args=("Pending",)
        orderdata=Sql(query,args)
        orderDataDisplay=orderdata.cursor.fetchall()
        print(orderDataDisplay)
        self.serial=0
        for i in orderDataDisplay:
            self.serial+=1
            self.tree.insert("","end",values=((self.serial),(i[0]),(i[1]),(i[2]),(i[3]+" {"+i[4]+"}")))
class ShopSummary():

    def __init__(self,master):
        self.master=master
        self.master.geometry('500x150')
        self.master.title('View Summary')

        self.Label = Label(self.master, text=("Hello "+Welcome.name+" This is the profit summary till now:-"),font=("Arial",17)).grid(row=0, column=0)
        self.viewSummary()

    def viewSummary(self):
        query="""SELECT OrderData.Item,OrderData.Quantity,ItemData.Price FROM OrderData INNER JOIN ItemData ON OrderData.Item=ItemData.Item WHERE OrderData.Completed=%s"""
        args=(Welcome.name,)
        summary=Sql(query,args)
        summaryDisplayData=summary.cursor.fetchall()
        print(summaryDisplayData)
        graphDict={}
        for x in summaryDisplayData:
            graphDict[x[0]]=0

        for x in summaryDisplayData:
            graphDict[x[0]]+=int(x[1])*int(x[2])
        print(graphDict)
        
        Xaxis=[x for x in graphDict]
        Yaxis=[graphDict[x] for x in graphDict]

        fig= plt.figure()
        plt.title("Profit Summary")
        plt.bar(Xaxis,Yaxis)
        plt.xlabel("Items")
        plt.ylabel("total earnings")
        plt.show()

root=Tk()
root.withdraw()
root1=Toplevel()
welcome=Welcome(root1)
root.mainloop()