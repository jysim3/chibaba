from os import path
import os.path
from item import Item
import sqlite3
from sqlite3 import Error
#from datetime import date

class Food(Item):
    expiryDate = None
    foodType = None

    def __init__(self, name, itemid, price, status=None, description=None, photo=None, userID=None, expiryDate=None, foodType=None):
        self.expiryDate = expiryDate
        self.foodType = foodType
        super().__init__(name, itemid, price, status, description, photo, userID, expiryDate, True)
        self.createSQL()
        self.injectUser()

    def getExpiryDate(self):
        return self.expiryDate

    def getFoodType(self):
        return self.foodType
    
    def setExpiryDate(self, expiryDate):
        self.expiryDate = expiryDate
        conn = Food.create_connection()
        with conn:
            task = (expiryDate, self.getID());
            sql = ''' UPDATE foods
                        SET expiryDate = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)
    
    def setFoodType(self, foodType):
        self.foodType = foodType
        conn = Food.create_connection()
        with conn:
            task = (foodType, self.getID());
            sql = ''' UPDATE foods
                        SET foodType = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)
    
        #SQL Stuff
    def createSQL(self):
        print("CALLED")

        conn = None
        try:
            conn = sqlite3.connect("chibaba.db")
        except Error as e:
            print(e)
            return
    
        sql_create_statement = """ CREATE TABLE IF NOT EXISTS foods (
                                        itemName text NOT NULL,
                                        itemID integer PRIMARY KEY,
                                        price integer NOT NULL,
                                        itemStatus text,
                                        itemDescription text,
                                        foodType text NOT NULL,
                                        expiryDate text NOT NULL,
                                        id integer NOT NULL,
                                        FOREIGN KEY (id) REFERENCES USER (userID)
                                    ); """

        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql_create_statement)
            except Error as e:
                print(e)
        else:
            print("CRITICAL FAILURE")
        
        conn.close()

    def injectUser(self):
        conn = None
        try:
            conn = sqlite3.connect("chibaba.db")
        except Error as e:
            print(e)
            return

        with conn:
            item = (self.name, self.itemId, self.price, self.status, self.description, self.foodType, self.expiryDate, self.userID);
            sql = ''' INSERT INTO foods(itemName, itemID, price, itemStatus, itemDescription, foodType, expiryDate, id)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
            curs = conn.cursor()
            curs.execute(sql, item)
        
        conn.close()
    
    @staticmethod
    def create_connection():
        conn = None
        try:
            conn = sqlite3.connect("chibaba.db")
            return conn
        except Error as e:
            print(e)

        return None
    

'''
Memes = Food("memes", 13, 400, "false", "false", "false", "04/15/29", "burgers")
Memes.setExpiryDate("04/19/59")
Memes.setFoodType("MEMELORD LEVEL")
'''