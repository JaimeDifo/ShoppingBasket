"""
Feature 3
Author: Jaime Difo Lorenzo
Student ID:  001101304
"""
from tkinter import *
from tkinter import ttk
import sqlite3
from os import *
from PIL import Image,ImageTk
from PIL import ImageGrab


from tkinter import *


"""
Global variable initialized
"""
global itemtotal

itemtotal = 0

def main():

    root = Tk()
    app = Welcome(root)
    totallist=[]
    bg = PhotoImage(file="Picture1.png")
    imglabel = Label(root, image=bg)
    imglabel.place(x=30, y=30)



    root.mainloop()

    """
    Class create to handle database creations and manipulation.
    """
class Database:
    """
    Function creates a table within the database if the shopping basket table does not exist.
    """
    def shoppingbaskettable(self):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "CREATE TABLE IF NOT EXISTS ShoppingBasket(Product text, ID integer , Price integer, " \
                "Quantity integer)"
        cursor.execute(query)
        con_database.commit()
        con_database.close()
    """
    Function to insert information from the GUI into the database.
    """
    def shoppingbasketinsert(self, Product, ID, Price, Quantity):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "INSERT INTO ShoppingBasket(Product, ID, Price, " \
                "Quantity) VALUES (?,?,?,?)"
        cursor.execute(query, (Product, ID, Price, Quantity))
        con_database.commit()
        con_database.close()
    """
    Function creates a table within the database if the shopping basket table does not exist.
    """
    def customertable(self):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "CREATE TABLE IF NOT EXISTS Customer(Name text, Age integer , Street text, " \
                "Postcode text, City text, Payment_method text, Card_number integer, " \
                "Issued_date text, Expiry_date text, Delivery text)"
        cursor.execute(query)
        con_database.commit()
        con_database.close()
    """
    Function to insert information from the GUI into the database.
    """
    def customerinsert(self, Name, Age, Street, Postcode, City, Payment_method, Card_number, issued_date, Expiry_date, Delivery):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "INSERT INTO Customer(Name, Age, Street, Postcode, City, Payment_method, Card_number, issued_date, " \
                "Expiry_date, Delivery) VALUES (?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (Name, Age, Street, Postcode, City, Payment_method, Card_number, issued_date, Expiry_date, Delivery))
        con_database.commit()
        con_database.close()
    """
    Function executes SQL in the database.
    """
    def ShoppingBasketSQL(self):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "SELECT * from ShoppingBasket"
        cursor.execute(query)
        rows= cursor.fetchall()
        con_database.commit()
        con_database.close()
        return rows
    """
    Function creates a table within the database if the shopping basket table does not exist.
    """
    def stock(self):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "CREATE TABLE IF NOT EXISTS Stock(Product text, ID integer , Price integer, " \
                "Quantity integer)"
        cursor.execute(query)
        con_database.commit()
        con_database.close()
    """
     Function executes SQL in the database.
    """
    def StockSQL(self):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "UPDATE Stock SET Quantity = Quantity - (SELECT Quantity from ShoppingBasket where ShoppingBasket.ID = " \
                "stock.ID) WHERE EXISTS ( SELECT Quantity from ShoppingBasket where ID = Stock.ID)"
        cursor.execute(query)
        stockupdate = cursor.fetchall()
        con_database.commit()
        con_database.close()
        return stockupdate
    """
    Function executes SQL in the database
    """
    def CustomerSQL(self):
        con_database = sqlite3.connect("Database.db")
        cursor = con_database.cursor()
        query = "SELECT * from Customer"
        cursor.execute(query)
        customer= cursor.fetchall()
        con_database.commit()
        con_database.close()
        return customer


class Welcome:
    """
    Class used as the main program window
    """
    def __init__(self, master):
        self.master = master
        self.master.geometry("461x350")
        self.master.title("Welcome to AAT!")
        self.master.configure(bg='white')
        self.frame = Frame(self.master) # Put this frame inside the window
        self.frame.grid(row=0, column=0, sticky="s")

        self.window2_btn = Button(self.master, text="Shop", command=self.page_two, width="15")
        self.window2_btn.grid(row = 0, column = 1)
        self.window3_btn = Button(self.master, text="Check-out", command=self.page_three, width="15")
        self.window3_btn.grid(row = 0, column = 2)
        self.window4_btn = Button(self.master, text="Display Receipt", command=self.page_four, width="15")
        self.window4_btn.grid(row = 0, column = 3)
        self.exit_btn = Button(self.master, text="Exit", command=exit, width="15")
        self.exit_btn.grid(row=0, column=4)

    """
    Function allows users to change windows within the GUI.
    """
    def page_two(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
    """
    Function allows users to change windows within the GUI.
    """
    def page_three(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
    """
    Function allows users to change windows within the GUI.
    """
    def page_four(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)


class Window2:
    """
    Class used to contain the online shop window
    """
    def __init__(self, master):
        self.master = master
        self.master.geometry("520x880")
        self.master.title("Online Shop!")
        self.master.configure(bg="lightblue")
        self.frame = Frame(self.master)
        self.frame.grid()

        self.dataconnect = Database()
        self.dataconnect.shoppingbaskettable()

        """
        Create Treeview Frame
        """
        self.tree_frame = Frame(self.frame)
        self.tree_frame.grid(pady=20)

        """
        Create Treeview
        """
        self.my_tree = ttk.Treeview(self.master)

        self.my_tree_shoppingbasket = ttk.Treeview(self.master)

        self.Store = Label(self.master, text="Online Store")
        self.Store.grid()

        """
        Grid to the screen
        """

        self.my_tree.grid()

        """
        Define the columns
        """
        self.my_tree['columns'] = ("Product", "ID", "Price","Quantity")

        """
        Format the columns
        """
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Product", anchor=W, width=140)
        self.my_tree.column("ID", anchor=CENTER, width=100)
        self.my_tree.column("Price", anchor=W, width=140)
        self.my_tree.column("Quantity", anchor=W, width=140)

        """
        Create headings
        """
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Product", text="Product", anchor=W)
        self.my_tree.heading("ID", text="ID", anchor=CENTER)
        self.my_tree.heading("Price", text="Price", anchor=W)
        self.my_tree.heading("Quantity", text="Quantity", anchor=W)

        """
        Add Data
        """
        data = [
            ["Bear", 1, 10, 1],
            ["Yo-Yo ", 2, 12, 1],
            ["Doll", 3, 15, 1],
            ["Train", 4, 8, 1],
            ["Puppet", 5, 9, 1],
            ["Ball", 6, 12, 1],
            ["Jump rope", 7, 21, 1],
            ["Spiderman", 8, 12, 1],
            ["Barbie", 9, 34, 1],
            ["Cars", 10, 24, 1],
        ]

        """
        Create striped row tags
        """
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        """
        Global variable initialized
        """
        global count
        count = 0

        """
        Create striped row tags
        """

        for record in data:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]),
                               tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]),
                               tags=('oddrow',))

            count += 1



        self.add_frame = Frame(self.master)
        self.add_frame.grid(pady=20)

        """
        Select Record
        """
        def select_record():
            """
            Clears entry boxes of the data they contain
            """
            name_box.delete(0, END)
            id_box.delete(0, END)
            price_box.delete(0, END)

            """
            Grab record number
            """
            selected = self.my_tree.focus()
            """
            Grab record values
            """
            values = self.my_tree.item(selected, 'values')

            """
            Output to entry boxes entered by user
            """
            name_box.insert(0, values[0])
            id_box.insert(0, values[1])
            price_box.insert(0, values[2])


        """
        Add record
        """
        def add_record():

            """
            Connects to the database and creates a stock table if it doesn't exist.
            """
            self.dataconnect = Database()
            self.dataconnect.stock()

            """
            Configures tag if odd to white and if even to lightblue
            """
            self.my_tree_shoppingbasket.tag_configure('oddrow', background="white")
            self.my_tree_shoppingbasket.tag_configure('evenrow', background="lightblue")

            """
            Set quantity to 1
            """
            quantity = 1

            global count

            """
            Create striped row tags
            """
            if count % 2 == 0:
                self.my_tree_shoppingbasket.insert(parent='', index='end', iid=count, text="",
                                              values=(name_box.get(), id_box.get(), price_box.get(), quantity), tags=('evenrow',))
            else:
                self.my_tree_shoppingbasket.insert(parent='', index='end', iid=count, text="",
                                              values=(name_box.get(), id_box.get(), price_box.get(), quantity), tags=('oddrow',))

            self.dataconnect.shoppingbasketinsert(name_box.get(), id_box.get(), price_box.get(), quantity)

            """
            Connects to database and executes the Stock SQL
            """
            self.dataconnect5 = Database()
            self.dataconnect5.StockSQL()

            """
            initialize cost to contain the price.
            """
            cost = price_box.get()

            """
            Converting the cost from a str into an int.
            """
            addtotal = int(cost)

            count += 1

            """
            Clear the boxes from the user data entered.
            """
            name_box.delete(0, END)
            id_box.delete(0, END)
            price_box.delete(0, END)

            class Baskettotaladd:
                """
                Class created to add the total of items added by the users and print to terminal.
                """
                def add_to_total(self, amount):
                    global itemtotal
                    itemtotal += amount

            """
            Calls on the class by initializing it to a variable then passing addtotal in the parameter to get the
            totals of items.
            """
            Baskettotaladd = Baskettotaladd()
            Baskettotaladd.add_to_total(addtotal)
            """
            Prints to screen
            """
            print("Shopping Basket total: £", itemtotal)


        """
        Remove one selected item in the list.
        """
        def remove_one():
            x = self.my_tree_shoppingbasket.selection()[0]
            self.my_tree_shoppingbasket.delete(x)


        """
        Save updated record into the shop or basket once amended.
        """
        def update_record():
            quantity = 1
            """
            Grab record number
            """
            selected = self.my_tree.focus()
            """
            Save new data
            """
            self.my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), price_box.get(),quantity))

            """
            Clear entry boxes
            """
            name_box.delete(0, END)
            id_box.delete(0, END)
            price_box.delete(0, END)

        """
        Create binding click function
        """
        def clicker(e):
            select_record()

        """
        Buttons created to call on the functions above
        """
        add_record = Button(self.master, text="Add Record", command=add_record)
        add_record.grid(pady=10)

        update_button = Button(self.master, text="Amend Record", command=update_record)
        update_button.grid(pady=10)

        remove_one = Button(self.master, text="Remove", command=remove_one)
        remove_one.grid(pady=10)

        """
        Label to identify the shopping basket.
        """
        Store = Label(self.master, text="Shopping Basket")
        Store.grid()

        """
        Define our columns
        """
        self.my_tree_shoppingbasket['columns'] = ("Product", "ID", "Price", "Quantity")

        """
        Formate our columns
        """
        self.my_tree_shoppingbasket.column("#0", width=0, stretch=NO)
        self.my_tree_shoppingbasket.column("Product", anchor=W, width=140)
        self.my_tree_shoppingbasket.column("ID", anchor=CENTER, width=100)
        self.my_tree_shoppingbasket.column("Price", anchor=W, width=140)
        self.my_tree_shoppingbasket.column("Quantity", anchor=W, width=140)

        """
        Create headings
        """
        self.my_tree_shoppingbasket.heading("#0", text="", anchor=W)
        self.my_tree_shoppingbasket.heading("Product", text="Product", anchor=W)
        self.my_tree_shoppingbasket.heading("ID", text="ID", anchor=CENTER)
        self.my_tree_shoppingbasket.heading("Price", text="Price", anchor=W)
        self.my_tree_shoppingbasket.heading("Quantity", text="Quantity", anchor=W)

        """
        Grids it to the screen
        """
        self.my_tree_shoppingbasket.grid()

        """
        Bindings
        """

        self.my_tree.bind("<ButtonRelease-1>", clicker)

        """
        Labels for the shopping window.
        """
        namel = Label(self.master, text="Name")
        namel.place(x=0, y=750)

        idl = Label(self.master, text="ID")
        idl.place(x=100, y=750)

        pricel = Label(self.master, text="Price")
        pricel.place(x=200, y=750)

        # Entry boxes
        name_box = Entry(self.master)
        name_box.place(x=0, y=770)

        id_box = Entry(self.master)
        id_box.place(x=100, y=770)

        price_box = Entry(self.master)
        price_box.place(x=200, y=770)

        self.window2_btn = Button(self.master, text="Return Home", command=self.exit_window)
        self.window2_btn.place(x=0, y=0)

        """
        Exit function.
        """
    def exit_window(self):
        self.master.destroy()


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1150x500")
        self.master.title("Check-out")
        self.master.configure(bg='lightblue')
        self.frame = Frame(self.master,bg='lightblue') # Put this frame inside the window
        self.frame.grid()

        """
        Connect to the database and executes the SQL.
        """
        self.dataconnect = Database()
        self.dataconnect.ShoppingBasketSQL()

        """
        Connect to the database and creates a customer table if it doesn't exist.
        """
        self.dataconnect2 = Database()
        self.dataconnect2.customertable()

        """
        Create frames for use.
        """
        self.body = Frame(self.frame, bg='lightblue')
        self.body.grid(row=0, column =1)
        self.detailsframe = Frame(self.frame, bg='lightblue')
        self.detailsframe.grid(row=0, column =0)
        self.button = Frame(self.frame, bg='lightblue')
        self.button.grid(row=1)
        self.treeviewframe = LabelFrame(self.body, text="Check out summary",bg='lightblue')
        self.treeviewframe.grid()

        """
        Headings for the Treeview are created.
        """
        self.treeview = ttk.Treeview(self.treeviewframe, columns=("Product", "ID", "Price", "Quantity"),
                                     show="headings")
        """
        Create Headings
        """
        self.treeview.heading("#0", text="", anchor=W)
        self.treeview.heading("Product", text="Product", anchor=W)
        self.treeview.heading("ID", text="ID", anchor=CENTER)
        self.treeview.heading("Price", text="Price", anchor=W)
        self.treeview.heading("Quantity", text="Quantity", anchor=W)

        """
        Create the columns for the treeview.
        """
        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("Product", anchor=W, width=140)
        self.treeview.column("ID", anchor=CENTER, width=100)
        self.treeview.column("Price", anchor=W, width=140)
        self.treeview.column("Quantity", anchor=W, width=140)

        """
        Grids to screen.
        """
        self.treeview.grid(ipadx=35, ipady=35)
        self.displaybtn = Button(self.button, text="Display List", command=self.displaydata).grid()

        """
        Creation of labels for the Check-out Window.
        """
        self.clientlabelname = Label(self.detailsframe, text="Enter your name:\n", bg='lightblue', relief="flat")
        self.clientlabelage = Label(self.detailsframe, text="Enter your age:\n", bg='lightblue', relief="flat")
        self.clientlabelstreet = Label(self.detailsframe, text="Enter your street:\n", bg='lightblue', relief="flat")
        self.clientlabelpostcode = Label(self.detailsframe, text="Enter your postcode:\n", bg='lightblue', relief="flat")
        self.clientlabelcity = Label(self.detailsframe, text="Enter your city:\n", bg='lightblue', relief="flat")
        self.clientlabelpaymentmethod = Label(self.detailsframe, text="Enter your payment method:\n", bg='lightblue',
                                              relief="flat")
        self.clientlabelcardnumber = Label(self.detailsframe, text="Enter your card number:\n", bg='lightblue', relief="flat")
        self.clientlabelissueddate = Label(self.detailsframe, text="Enter your card's issued date:\n", bg='lightblue',
                                           relief="flat")
        self.clientlabelexpiry = Label(self.detailsframe, text="Enter your card's expiry date:\n", bg='lightblue',
                                       relief="flat")
        self.deliveryto = Label(self.detailsframe, text="Delivery to:\n", bg='lightblue', relief="flat")


        """
        Creation of boxes for the customer check out window.
        """
        self.client_namebox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_namebox.grid(row=2, column=3, sticky="ne")
        self.client_agebox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_agebox.grid(row=4, column=3, sticky="ne")

        self.client_streetbox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_streetbox.grid(row=6, column=3, sticky="ne")
        self.client_postcodebox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_postcodebox.grid(row=8, column=3, sticky="ne")
        self.client_citybox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_citybox.grid(row=10, column=3, sticky="ne")

        self.client_paymentmethodbox = Entry(self.detailsframe, width=50, bg='lightblue', justify="right")
        self.client_paymentmethodbox.grid(row=12, column=3, sticky="ne")
        self.client_cardnumberbox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_cardnumberbox.grid(row=14, column=3, sticky="ne")
        self.client_issueddatebox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_issueddatebox.grid(row=16, column=3, sticky="ne")
        self.client_expirybox = Entry(self.detailsframe, width=50, bg='lightblue')
        self.client_expirybox.grid(row=18, column=3, sticky="ne")

        """
        Buttons and dropdown list for the customers.
        """
        self.clientButton = Button(self.detailsframe, text="Enter", command=self.addclientdetails)

        self.clicked = StringVar()
        self.dropdownmenu = OptionMenu(self.detailsframe, self.clicked, "Home", "Neighbour's address", "Store", "P.O Box")
        self.clicked.set("Home")

        self.delivery = self.dropdownmenu
        self.dropdownmenu.grid(row=20, column=3, sticky="ne")
        self.clientButton.grid(row=21, column=3, sticky="ne")

        """
        Grids to screen.
        """

        self.clientlabelname.grid(row=2, column=2, sticky="ne")
        self.clientlabelage.grid(row=4, column=2, sticky="ne")
        self.clientlabelstreet.grid(row=6, column=2, sticky="ne")
        self.clientlabelstreet.grid(row=6, column=2, sticky="ne")
        self.clientlabelpostcode.grid(row=8, column=2, sticky="ne")
        self.clientlabelcity.grid(row=10, column=2, sticky="ne")
        self.clientlabelpaymentmethod.grid(row=12, column=2, sticky="ne")
        self.clientlabelcardnumber.grid(row=14, column=2, sticky="ne")
        self.clientlabelissueddate.grid(row=16, column=2, sticky="ne")
        self.clientlabelexpiry.grid(row=18, column=2, sticky="ne")
        self.deliveryto.grid(row=20, column=2, sticky="ne")

        """
        Creation of return home button.
        """

        self.window2_btn = Button(self.detailsframe, text="Return Home", command=self.exit_window).grid(row=0, column=0)

        global itemtotal

        """
        Add shipping price to toal
        """
        if self.clicked.get() == "Home":
            global itemtotal
            int(itemtotal)
            itemtotal += 3
            if self.clicked.get() == "Neighbour's address":
                int(itemtotal)
                itemtotal += 4
                if self.clicked.get() == "Store":
                    int(itemtotal)
                    itemtotal += 0
                    if self.clicked.get() == "P.O Box":
                        int(itemtotal)
                        itemtotal += 3



    def addclientdetails(self):
        """
        Connect to the database and insert data into the customer table.
        """
        self.dataconnect3 = Database()
        self.dataconnect3.customerinsert(self.client_namebox.get(), self.client_agebox.get(),
                                         self.client_streetbox.get(),
                                         self.client_postcodebox.get(), self.client_citybox.get(),
                                         self.client_paymentmethodbox.get(),
                                         self.client_cardnumberbox.get(), self.client_issueddatebox.get(),
                                         self.client_expirybox.get(),
                                         self.clicked.get())

        """
        Create global variables
        """
        global customername
        global customerage
        global customerstreet
        global customerpostcode
        global customercity
        global customerpaymentmethod
        global customercardnumber
        global customerissueddate
        global customerexpirydate
        global customerdelivery

        """
        Initialize the variables to str
        """
        customername = ""
        customerage = ""
        customerstreet = ""
        customerpostcode = ""
        customercity = ""
        customerpaymentmethod = ""
        customercardnumber = ""
        customerissueddate = ""
        customerexpirydate = ""
        customerdelivery = ""

        """
        Initialize variables to user input data.
        """
        customername = self.client_namebox.get()
        customerage = self.client_agebox.get()
        customerstreet = self.client_streetbox.get()
        customerpostcode = self.client_postcodebox.get()
        customercity = self.client_citybox.get()
        customerpaymentmethod = self.client_paymentmethodbox.get()
        customercardnumber = self.client_cardnumberbox.get()
        customerissueddate = self.client_issueddatebox.get()
        customerexpirydate = self.client_expirybox.get()
        customerdelivery = self.clicked.get()

        """
        Calls on the VISACheck function to ensure the cardnumber is only integer.
        """
        cardnumber = self.client_cardnumberbox.get()
        errormessage = Errorwindow
        errormessage.VISACheck(cardnumber)

        """
        Class created to add the total of items added by the users and print to terminal.
        """
        global itemtotal
        int(itemtotal)
        print("Total + Shipping: £", itemtotal)

    def displaydata(self):
        """
        Function displays shopping list on the check-out window.
        """
        global result

        items = self.dataconnect.ShoppingBasketSQL()

        for result in items:
            self.treeview.insert("", END, values=result)


    def exit_window(self):
        """
        Function exits window.
        """
        self.master.destroy()

class Errorwindow:
    def VISACheck(cardnumber):
        """
         Function checks that cardnumber is entered as an integer.
        """
        if cardnumber.isdigit() == True:
            print("Payment has been accepted")
        else:
            print("Payment has not been accepted")


class Window4:
    def __init__(self, master):
        """
         Print Receipt window initialization
        """
        self.master = master
        self.master.geometry("600x500")
        self.master.title( "Display Receipt")
        self.master.configure(bg="Lightblue")
        self.frame = Frame(self.master) # Put this frame inside the window
        self.frame.grid()

        """
        Connect to database and execute SQL code for customer table.
        """
        self.dataconnect6 = Database()
        self.dataconnect6.CustomerSQL()

        """
        Connect to database and create stock table if it doesn't exist.
        """
        self.dataconnect7 = Database()
        self.dataconnect7.stock()

        """
        Create label and grid to screen. Then initialize treeview.
        """
        self.treeviewframe = LabelFrame(self.master, text="Shopping List", bg='lightblue')
        self.treeviewframe.grid()

        self.treeview = ttk.Treeview(self.treeviewframe, columns=("Product", "ID", "Price", "Quantity"),
                                     show="headings")

        """
        Create Headings
        """
        self.treeview.heading("#0", text="", anchor=W)
        self.treeview.heading("Product", text="Product", anchor=W)
        self.treeview.heading("ID", text="ID", anchor=CENTER)
        self.treeview.heading("Price", text="Price", anchor=W)
        self.treeview.heading("Quantity", text="Quantity", anchor=W)

        """
        Formate our columns
        """
        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("Product", anchor=W, width=140)
        self.treeview.column("ID", anchor=CENTER, width=100)
        self.treeview.column("Price", anchor=W, width=140)
        self.treeview.column("Quantity", anchor=W, width=140)

        """
        Grid to screen
        """
        self.treeview.grid(ipadx=35, ipady=35)

        """
        Connect to the database and execute Shopping Basket SQL.
        """
        self.dataconnect7 = Database()
        self.dataconnect7.ShoppingBasketSQL()

        items = self.dataconnect7.ShoppingBasketSQL()

        for i in items:
            self.treeview.insert("", END, values=i)

        """
        Display clients customer information on the GUI
        """

        recieptlabel = Label(self.master, text="Client's Details\n"
                                               " Name: " + customername +
                                               "\n Age: " + customerage +
                                               "\n Address: " + customerstreet + " " + customerpostcode + " " + customercity +
                                               "\n Card Details: " + customercardnumber + " " + customerpaymentmethod +
                                               "\n Card Issued Date: " + customerissueddate + " "
                                               "\n Card Expiry Date: " + customerexpirydate + " "
                                               "\n Deliver to: " + customerdelivery + " "
                             , bg='lightblue')

        recieptlabel.grid()


        """
        Create button and grid to screen.
        """
        self.print_btn = Button(self.master, text="Print Receipt", command=printreceipt)
        self.print_btn.grid()

        self.window2_btn = Button(self.master, text="Return Home", command=exit_window)
        self.window2_btn.grid()

def printreceipt():
    snapshot = ImageGrab.grab()
    save_path = "C:\\Users\\Jaime Difo\\PycharmProjects\\fixed\\Receipt.jpg"
    snapshot.save(save_path)

def exit_window(self):
     self.master.destroy()

if __name__ == '__main__':
    main()
