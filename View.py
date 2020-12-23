import tkinter as tk
from tkinter import *
from tkinter import ttk
import Controller as c
import Model as m


class view:

    def showUpdatedCars():
        updatedCars = tk.Tk()
        updatedCars.title("Updated Cars List")
        tree = ttk.Treeview(updatedCars)
        tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")
        tree.column("#0", width=80, minwidth=50, stretch=tk.NO)
        tree.column("one", width=80, minwidth=50, stretch=tk.NO)
        tree.column("two", width=80, minwidth=50, stretch=tk.NO)
        tree.column("three", width=80, minwidth=50, stretch=tk.NO)
        tree.column("four", width=80, minwidth=50, stretch=tk.NO)
        tree.column("five", width=80, minwidth=50, stretch=tk.NO)
        tree.column("six", width=80, minwidth=50, stretch=tk.NO)
        tree.column("seven", width=80, minwidth=50, stretch=tk.NO)
        tree.column("eight", width=80, minwidth=50, stretch=tk.NO)

        tree.heading("#0", text="Car ID", anchor=tk.W)
        tree.heading("one", text="Year", anchor=tk.W)
        tree.heading("two", text="Condition", anchor=tk.W)
        tree.heading("three", text="Make", anchor=tk.W)
        tree.heading("four", text="Model", anchor=tk.W)
        tree.heading("five", text="Color", anchor=tk.W)
        tree.heading("six", text="Mileage(miles)", anchor=tk.W)
        tree.heading("seven", text="Price", anchor=tk.W)
        tree.heading("eight", text="Dealer ID", anchor=tk.W)

        mo1 = m.model()
        carList = mo1.listOfCars()

        for i in carList:
            tree.insert('', 'end', text=i[0], values=(i[4], i[3], i[5], i[7], i[6], str(i[8]), i[1], i[2]))

        tree.pack(side=tk.TOP, fill=tk.X)

    def updateCar():
        global updateCarPage
        updateCarPage = tk.Tk()
        dealerPage.destroy()
        updateCarPage.title('Update Car')
        updateCarPage.geometry('727x379')
        lblCarID = Label(updateCarPage, text="Enter the ID the car you would like to update: ")
        lblCarID.place(x=0, y=0)
        lblCarID.config(font=('Times New Roman', 12))
        txtCarID = Entry(updateCarPage, bd=3)
        txtCarID.place(x=290, y=0)
        butDel = tk.Button(updateCarPage, text="Delete this Car",
                           command=lambda: c1.deleteCar(txtCarID.get()))
        butDel.pack()
        butDel.place(x=390, y=0)
        lblUpd = Label(updateCarPage, text="Select the attribute you would like to update: ")
        lblUpd.place(x=0, y=50)
        lblUpd.config(font=('Times New Roman', 12))
        cmbAtt = ttk.Combobox(updateCarPage, values=["Year", "Model", "Make", "Price", "Color", "Condition", "Mileage"],
                              width='10')
        cmbAtt.place(x=290, y=50)
        cmbAtt.current(0)
        lblVal = Label(updateCarPage, text="Enter the updated value of the attribute : ")
        lblVal.place(x=0, y=100)
        lblVal.config(font=('Times New Roman', 12))
        txtVal = Entry(updateCarPage, bd=3)
        txtVal.place(x=290, y=100)

        tree = ttk.Treeview(updateCarPage)
        tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")
        tree.column("#0", width=80, minwidth=50, stretch=tk.NO)
        tree.column("one", width=80, minwidth=50, stretch=tk.NO)
        tree.column("two", width=80, minwidth=50, stretch=tk.NO)
        tree.column("three", width=80, minwidth=50, stretch=tk.NO)
        tree.column("four", width=80, minwidth=50, stretch=tk.NO)
        tree.column("five", width=80, minwidth=50, stretch=tk.NO)
        tree.column("six", width=80, minwidth=50, stretch=tk.NO)
        tree.column("seven", width=80, minwidth=50, stretch=tk.NO)
        tree.column("eight", width=80, minwidth=50, stretch=tk.NO)

        tree.heading("#0", text="Car ID", anchor=tk.W)
        tree.heading("one", text="Year", anchor=tk.W)
        tree.heading("two", text="Condition", anchor=tk.W)
        tree.heading("three", text="Make", anchor=tk.W)
        tree.heading("four", text="Model", anchor=tk.W)
        tree.heading("five", text="Color", anchor=tk.W)
        tree.heading("six", text="Mileage(miles)", anchor=tk.W)
        tree.heading("seven", text="Price", anchor=tk.W)
        tree.heading("eight", text="Dealer ID", anchor=tk.W)

        m1 = m.model()
        carList = m1.listOfCars()

        for i in carList:
            tree.insert('', 'end', text=i[0], values=(i[4], i[3], i[5], i[7], i[6], str(i[8]), i[1], i[2]))

        tree.place(x=1, y=150)

        butsub = tk.Button(updateCarPage, text="Submit",
                           command=lambda: c1.updateCar(txtCarID.get(), cmbAtt.get(), txtVal.get()))
        butsub.pack()
        butsub.place(x=500, y=100)

    def addNewCar():
        global addCarPage
        addCarPage = tk.Tk()
        dealerPage.destroy()
        addCarPage.title('Add Car')
        addCarPage.geometry('200x310')
        lblYear = Label(addCarPage, text="Year : ")
        lblYear.place(x=0, y=0)
        lblYear.config(font=('Times New Roman', 12))
        txtYear = Entry(addCarPage, bd=3)
        txtYear.place(x=50, y=0)
        lblMake = Label(addCarPage, text="Make : ")
        lblMake.place(x=0, y=40)
        lblMake.config(font=('Times New Roman', 12))
        txtMake = Entry(addCarPage, bd=3)
        txtMake.place(x=50, y=40)
        lblModel = Label(addCarPage, text="Model : ")
        lblModel.place(x=0, y=80)
        lblModel.config(font=('Times New Roman', 12))
        txtModel = Entry(addCarPage, bd=3)
        txtModel.place(x=60, y=80)
        lblMile = Label(addCarPage, text="Mileage : ")
        lblMile.place(x=0, y=120)
        lblMile.config(font=('Times New Roman', 12))
        txtMile = Entry(addCarPage, bd=3)
        txtMile.place(x=65, y=120)
        lblPrice = Label(addCarPage, text="Price : ")
        lblPrice.place(x=0, y=160)
        lblPrice.config(font=('Times New Roman', 12))
        txtPrice = Entry(addCarPage, bd=3)
        txtPrice.place(x=50, y=160)
        lblCond = Label(addCarPage, text="Condition : ")
        lblCond.place(x=0, y=200)
        lblCond.config(font=('Times New Roman', 12))
        txtCond = Entry(addCarPage, bd=3)
        txtCond.place(x=70, y=200)
        lblColor = Label(addCarPage, text="Color : ")
        lblColor.place(x=0, y=240)
        lblColor.config(font=('Times New Roman', 12))
        txtColor = Entry(addCarPage, bd=3)
        txtColor.place(x=60, y=240)
        butAddCar = tk.Button(addCarPage, text="Submit",
                              command=lambda: c1.addCar(txtYear.get(), txtMake.get(), txtModel.get(),
                                                        txtMile.get(), txtPrice.get(), txtCond.get(),
                                                        txtColor.get()))
        butAddCar.pack()
        butAddCar.place(x=80, y=280)

    def afterLogin():
        global dealerPage
        dealerPage = tk.Tk()
        dealerLoginPage.destroy()
        dealerPage.title("Dealer")
        lblPrompt = Label(dealerPage, text="Please select next step: ")
        lblPrompt.place(x=0, y=0)
        lblPrompt.config(font=("Times New Roman", 15))
        dealerPage.geometry('200x150')
        but_update = tk.Button(dealerPage, text="Update car", command=view.updateCar)
        but_update.pack()
        but_update.place(x=62, y=90)
        but_new = tk.Button(dealerPage, text="Add car", command=view.addNewCar)
        but_new.pack()
        but_new.place(x=70, y=50)

    def dealerLoginWindow():
        global dealerLoginPage
        dealerLoginPage = tk.Tk()
        dealerLoginPage.title("Dealer Login Page")
        root.destroy()
        dealerLoginPage.geometry('300x300')
        tbUser = Entry(dealerLoginPage, bd=3)
        tbUser.place(x=80, y=50)
        lUser = Label(dealerLoginPage, text="Username")
        lUser.place(x=110, y=25)
        tbPass = Entry(dealerLoginPage, show="*", bd=3)
        tbPass.place(x=80, y=140)
        lPass = Label(dealerLoginPage, text="Password")
        lPass.place(x=110, y=115)
        global c1
        c1 = c.controller()
        butSub = tk.Button(dealerLoginPage, text="Login",
                           command=lambda: c1.login(tbUser.get(), tbPass.get()))
        butSub.pack()
        butSub.place(x=125, y=200)
        dealerLoginPage.mainloop()

    def customerWindow():
        customerPage = tk.Tk()
        root.destroy()
        customerPage.title('Customer Page')
        customerPage.geometry('400x160')
        lblAtt = Label(customerPage, text="Select the attribute you would like to filter for: ")
        lblAtt.place(x=0, y=00)
        lblAtt.config(font=('Times New Roman', 12))
        cmbAtt = ttk.Combobox(customerPage, values=["Year", "Model", "Make", "Price", "Color", "Condition", "Mileage"],
                              width='10')
        cmbAtt.place(x=290, y=00)
        cmbAtt.current(0)
        lblVal = Label(customerPage, text="Enter the filter value for the attribute : ")
        lblVal.place(x=0, y=50)
        lblVal.config(font=('Times New Roman', 12))
        lblInfo = Label(customerPage, text="(For year, price and mileage. You will be entering the maximum value to "
                                           "filter.)")
        lblInfo.place(x=0, y=70)
        lblInfo.config(font=('Times New Roman', 9))
        lblInfo2 = Label(customerPage, text="P.S. Enter 'Show All' to see all cars in the Database.")
        lblInfo2.place(x=0, y=90)
        lblInfo2.config(font=('Times New Roman', 11))
        txtVal = Entry(customerPage, bd=3)
        txtVal.place(x=250, y=50)
        txtVal.insert(0, "Show All")
        c2 = c.controller()
        but_Sub = tk.Button(customerPage, text="Submit",
                            command=lambda: c2.searchForCars(cmbAtt.get(), txtVal.get()))
        but_Sub.pack()
        but_Sub.place(x=150, y=120)

    def afterSearch(resList):
        afterSPg = tk.Tk()
        afterSPg.title("Search Result")
        tree = ttk.Treeview(afterSPg)
        tree["columns"] = ("one", "two", "three", "four", "five", "six")
        tree.column("#0", width=80, minwidth=50, stretch=tk.NO)
        tree.column("one", width=80, minwidth=50, stretch=tk.NO)
        tree.column("two", width=80, minwidth=50, stretch=tk.NO)
        tree.column("three", width=80, minwidth=50, stretch=tk.NO)
        tree.column("four", width=80, minwidth=50, stretch=tk.NO)
        tree.column("five", width=80, minwidth=50, stretch=tk.NO)
        tree.column("six", width=80, minwidth=50, stretch=tk.NO)

        tree.heading("#0", text="Year", anchor=tk.W)
        tree.heading("one", text="Condition", anchor=tk.W)
        tree.heading("two", text="Make", anchor=tk.W)
        tree.heading("three", text="Model", anchor=tk.W)
        tree.heading("four", text="Color", anchor=tk.W)
        tree.heading("five", text="Mileage", anchor=tk.W)
        tree.heading("six", text="Price", anchor=tk.W)

        print(resList)
        for i in resList:
            tree.insert('', 'end', text=i[4], values=(i[3], i[5], i[7], i[6], i[8], i[1]))

        tree.pack(side=tk.TOP, fill=tk.X)

    def run():
        global root
        root = tk.Tk()
        root.title("Main")
        L1 = Label(root, text="Please select user type: ")
        L1.place(x=0, y=0)
        L1.config(font=("Times New Roman", 15))
        root.geometry('200x150')
        but_dealer = tk.Button(root, text="Dealer", command=view.dealerLoginWindow)
        but_dealer.pack()
        but_dealer.place(x=80, y=50)
        but_customer = tk.Button(root, text="Customer", command=view.customerWindow)
        but_customer.pack()
        but_customer.place(x=70, y=90)

        root.mainloop()
