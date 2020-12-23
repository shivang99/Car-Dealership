import Model as m
import View as v
from tkinter import *
from tkinter import messagebox
import random


class controller:
    def __init__(self):
        self.view = v.view
        self.userId = 0

    def login(self, user, pwd):
        m1 = m.model()
        userLis = m1.listOfUsers()
        match = False
        for x in userLis:
            if user == x[0]:
                if pwd == x[1]:
                    v.view.afterLogin()
                    match = True
                    self.userId = user
        if not match:
            master = Tk()
            messagebox.showerror("Error", "Wrong Username and/or Password")
            master.withdraw()

    def addCar(self, year, make, model, mile, price, cond, color):
        m1 = m.model()
        id = random.randint(100, 1000)
        if m1.addCar(id, year, make, model, color, cond, price, self.userId, mile):
            self.view.showUpdatedCars()

    def updateCar(self, id, att, val):
        m3 = m.model()
        if m3.updateDB(id, att, val):
            self.view.showUpdatedCars()

    def deleteCar(self, id):
        m2 = m.model()
        if m2.delACar(int(id)):
            self.view.showUpdatedCars()

    def searchForCars(self, att, value):
        m4 = m.model()
        self.view.afterSearch(m4.searchCars(att, value))


if __name__ == "__main__":
    con = controller()
    con.view.run()
