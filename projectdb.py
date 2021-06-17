from os import name
import sqlite3

class Database:
    def __init__(self,projectdb):
        self.conn = sqlite3.connect(projectdb)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(EmployeeID integer PRIMARY KEY, Car text, ClockIn text, ClockOut text,Date text)")
        pass
    
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self,EmployeeID,Car,ClockIn,ClockOut,Date):
        self.cur.execute("INSERT INTO parts VALUES (NULL,?,?,?,?)",(Car,ClockIn,ClockOut,Date))
        self.conn.commit()

    def remove(self, EmployeeID):
        self.cur.execute("DELETE FROM parts WHERE EmployeeID=?", 
                         (EmployeeID,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    
      

        
#projectdb=Database('employee.db')
#projectdb.insert("1", "Proton", "8:00", "5:30", "17")
#projectdb.insert("2", "Saga", "7:00", "5:30", "17")
#projectdb.insert("3", "Toyota", "7:30", "5:30", "17")
#projectdb.insert("4", "Viva", "8:30", "5:30", "17")
#projectdb.insert("5", "Myvi", "11:00", "5:30", "17")
#projectdb.insert("6", "Hilax", "11:30", "5:30", "17")
