import os.path
from os import path
import sqlite3
from sqlite3 import Error

class Item:
    name = None
    itemId = 0
    price = 0.0
    #0 for not being sold right npw
    #1 for selling
    #2 for sold
    status = 0
    description = None
    photo = None
    userID = None
    buyerID = None

    #ItemID should not be set by the user, FIXME
    def __init__(self, name, price, status=None, description=None, photo=None, userID=None, foodFlag=False):
        #print("Called parent's constructor")
        self.name = name
        self.price = price
        self.status = status
        self.description = description
        self.photo = photo 
        self.userID = userID
        self.buyerID = None
        if (foodFlag == False):
            result0 = self.createSQL()
            lastUID = self.injectItem()
            if (result0 is None or lastUID is None):
                return None

    def getName(self):
        return self.name
    
    def getID(self):
        return self.itemId

    def getPrice(self):
        return self.price
    
    def getStatus(self):
        return self.status

    def getDescription(self):
        return self.description

    def getPhoto(self):
        return self.photo

    @staticmethod 
    def getAllItems():
        conn = Item.create_connection()
        with conn:
            sql = "SELECT * from items"
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

            result = [x for x in cur.fetchall()]
            return result, cur.description

    @staticmethod
    def setName(itemID, name):
        conn = Item.create_connection()
        with conn:
            task = (name, itemID);
            sql = ''' UPDATE items
                        SET itemName = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

    @staticmethod
    def setPrice(itemID, price):
        conn = Item.create_connection()
        with conn:
            task = (price, itemID);
            sql = ''' UPDATE items
                        SET price = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

    @staticmethod
    def setStatus(itemID, status):
        conn = Item.create_connection()
        with conn:
            task = (status, itemID);
            sql = ''' UPDATE items
                        SET itemStatus = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

    @staticmethod
    def setDescription(itemID, description):
        conn = Item.create_connection()
        with conn:
            task = (description, itemID);
            sql = ''' UPDATE items
                        SET itemDescription = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)
    
    @staticmethod
    def setBuyer(itemID, buyerID):
        if Item.getItem(itemID) == None:
            return False
        conn = Item.create_connection()
        with conn:
            task = (buyerID, itemID);
            sql = ''' UPDATE items
                        SET buyerID = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)
            return True
    '''
    def setPhoto(self, photo):
        self.photo = photo
    '''

    #SQL Stuff
    def createSQL(self):
        print("CALLED")
        '''
        if (path.exists("chibaba.db") == True):
            #print("Entered here")
            return
        '''

        conn = None
        try:
            conn = sqlite3.connect("chibaba.db")
        except Error as e:
            print(e)
            return False
    
        sql_create_statement = """ CREATE TABLE IF NOT EXISTS items (
                                        itemName text NOT NULL,
                                        itemID integer PRIMARY KEY AUTOINCREMENT,
                                        price integer NOT NULL,
                                        itemStatus text,
                                        itemDescription text,
                                        buyerID integer,
                                        id integer NOT NULL,
                                        FOREIGN KEY (id) REFERENCES USER (userID)
                                    ); """

        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql_create_statement)
            except Error as e:
                print(e)
                return False
        else:
            print("CRITICAL FAILURE")
            return False
        conn.close()

    def injectItem(self):
        conn = None
        try:
            conn = sqlite3.connect("chibaba.db")
        except Error as e:
            print(e)
            return

        lastUID = None
        with conn:
            item = (self.name, self.price, self.status, self.description, self.userID, None);
            sql = ''' INSERT INTO items(itemName, price, itemStatus, itemDescription, id, buyerID)
                        VALUES(?, ?, ?, ?, ?, ?) '''
            curs = conn.cursor()
            lastUID = curs.execute(sql, item).lastrowid

        self.itemId = lastUID
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

    @staticmethod
    def getItem(itemID):
        conn = Item.create_connection()
        if (conn == None):
            return None
        
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM items WHERE itemID=?", (itemID, ))
            return cur.fetchone()

        return None

    @staticmethod
    def addItems(name, price, status, description, photo, userID):
        item = Item(name, price, status, description, None, userID)
        if (item is None):
            return None
        return item.getID()

if __name__ == '__main__':
    memes = Item("Memes", 500, 0, "The end of the memes", None, 11111111)
    memes2 = Item("memes, the second coming", 450, 0, "The resurrection", None, 5161616)
    memes3 = Item("BATTLESTAR GALACTICA", 5000, 0, "Battlestar is pretty lit", None, 5161616)
