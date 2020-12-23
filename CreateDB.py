import sqlite3
def presetup():
    conn = sqlite3.connect('car.db')
    c = conn.cursor()

    #---------------------------- DEALER DB------------------------------
    c.execute('''DROP TABLE IF EXISTS dealer''')

    c.execute('''
            CREATE TABLE dealer
            (did VARCHAR(10),
            dpas VARCHAR(30),
            CONSTRAINT pdk PRIMARY KEY(did))''')

    c.execute("INSERT INTO dealer VALUES ('user1','User#1')")
    c.execute("INSERT INTO dealer VALUES ('user2','User#2')")
    c.execute("INSERT INTO dealer VALUES ('user3','User#3')")

    #---------------------------- CARS DB------------------------------
    c.execute('''DROP TABLE IF EXISTS cars''')    
    c.execute('''
            CREATE TABLE cars(cid INT(3) NOT NULL,
            Price DECIMAL(10,2) NOT NULL, 
            did VARCHAR(10),
            Condition CHAR(5) NOT NULL DEFAULT 'New',
            Year INT(4),
            Make CHAR(25) NOT NULL, 
            Color CHAR(25) DEFAULT 'White' NOT NULL,
            Model VARCHAR(20) NOT NULL, 
            Mileage DECIMAL(10,2),
            CONSTRAINT pck PRIMARY KEY(cid),
            CONSTRAINT fck FOREIGN KEY(did) REFERENCES dealer(did)
            )''')

    c.execute("INSERT INTO cars VALUES (123, 19500.00, 'user1', 'Used', 2017, 'Toyota', 'Red', 'Camry', 53500.21)")
    c.execute("INSERT INTO cars VALUES (456, 40000.00, 'user2', 'New', 2020, 'Hyundai', 'Silver', 'Palisade', 0)")
    c.execute("INSERT INTO cars VALUES (789, 21000.00, 'user2', 'New', 2020, 'Honda', 'Blue', 'Civic', 0)")
    c.execute("INSERT INTO cars VALUES (912, 30500.00, 'user3', 'Used', 2018, 'Audi', 'Black', 'Q5', 33500)")
    c.execute("INSERT INTO cars VALUES (345, 80000.00, 'user3', 'New', 2020, 'Tesla', 'Gold', 'Model x', 0)")
    conn.commit()
    conn.close()
    return 

if __name__ == "__main__":
    presetup()
    conn = sqlite3.connect('car.db')
    c = conn.cursor()
    t = ('user1',)    
    c.execute('SELECT * FROM cars')
    print(c.fetchall())
    c.execute('SELECT * FROM dealer')
    print(c.fetchall())
    c.execute('SELECT * FROM cars')
    print(c.fetchall())