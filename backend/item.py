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

    #ItemID should not be set by the user, FIXME
    def __init__(self, name, itemid, price, status=None, description=None, photo=None, foodFlag=False):
        #print("Called parent's constructor")
        self.name = name
        self.itemId = itemid
        self.price = price
        self.status = 0
        self.description = description
        self.photo = photo 
        if (foodFlag == False):
            self.createSQL()
            self.injectUser()

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

    def setName(self, name):
        self.name = name
        conn = Item.create_connection()
        with conn:
            task = (name, self.getID());
            sql = ''' UPDATE items
                        SET itemName = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

    def setPrice(self, price):
        self.price = price
        conn = Item.create_connection()
        with conn:
            task = (price, self.getID());
            sql = ''' UPDATE items
                        SET price = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

    def setStatus(self, status):
        self.status = status
        conn = Item.create_connection()
        with conn:
            task = (status, self.getID());
            sql = ''' UPDATE items
                        SET itemStatus = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

    def setDescription(self, description):
        self.description = description
        conn = Item.create_connection()
        with conn:
            task = (description, self.getID());
            sql = ''' UPDATE items
                        SET itemDescription = ?
                    WHERE itemID = ?'''
            cur = conn.cursor()
            cur.execute(sql, task)

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
            return
    
        sql_create_statement = """ CREATE TABLE IF NOT EXISTS items (
                                        itemName text NOT NULL,
                                        itemID integer PRIMARY KEY,
                                        price integer NOT NULL,
                                        itemStatus text,
                                        itemDescription text
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
            item = (self.name, self.itemId, self.price, self.status, self.description);
            sql = ''' INSERT INTO items(itemName, itemID, price, itemStatus, itemDescription)
                        VALUES(?, ?, ?, ?, ?) '''
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
memes = Item("Memes", 123, 500, 0, "The end of the memes", None)
memes.setName("mewrmwe")
memes.setStatus(2)
memes.setPrice(400)
#print(memes.getName())
'''