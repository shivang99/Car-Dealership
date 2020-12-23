import sqlite3


class model:
    def __init__(self, db="car.db"):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def listOfUsers(self):
        self.cur.execute('SELECT * FROM dealer')
        return self.cur.fetchall()

    def listOfCars(self):
        self.cur.execute('SELECT * FROM cars')
        return self.cur.fetchall()

    def addCar(self, i, y, ma, mo, col, con, p, di, mi):
        self.cur.execute(
            "INSERT INTO cars VALUES ({0}, {1}, '{2}', '{3}', {4}, '{5}', '{6}', '{7}', {8})".format(int(i), float(p),
                                                                                                     str(di), str(con),
                                                                                                     int(y), str(ma),
                                                                                                     str(col), str(mo),
                                                                                                     float(mi)))
        self.conn.commit()
        self.conn.close()
        return True

    def updateDB(self, id, at, value):
        if at == 'Year':
            self.cur.execute("UPDATE cars SET {0} = {1} WHERE cid = {2}".format(at, int(value), id, ))
        elif at == 'Mileage' or at == 'Price':
            self.cur.execute("UPDATE cars SET {0} = {1} WHERE cid = {2}".format(at, float(value), id, ))
        else:
            self.cur.execute("UPDATE cars SET {0} = '{1}' WHERE cid = {2}".format(at, value, id, ))
        self.conn.commit()
        self.conn.close()
        return True

    def delACar(self, id):
        self.cur.execute("DELETE FROM cars WHERE cid={}".format(int(id)))
        self.conn.commit()
        self.conn.close()
        return True

    def searchCars(self, att, val):
        if val == "Show All":
            self.cur.execute('SELECT * FROM cars')
        elif att == 'Year':
            self.cur.execute("SELECT * FROM cars WHERE {0} BETWEEN 0 AND {1}".format(att, int(val)))
        elif att == 'Mileage' or att == 'Price':
            self.cur.execute("SELECT * FROM cars WHERE {0} BETWEEN 0.0 AND {1}".format(att, float(val)))
        else:
            self.cur.execute("SELECT * FROM cars WHERE {0} = '{1}'".format(att, str(val)))

        return self.cur.fetchall()
