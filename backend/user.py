import os
import random
import sqlite3
from sqlite3 import Error
import json 
import datetime,re
from item import Item

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        create_table_user = """CREATE TABLE IF NOT EXISTS USER(
                                        userID integer primary key,
                                        userName text,
                                        password text,
                                        creation_time time,
                                        item text references items(itemID)
                                    ); """
        cur = conn.cursor()
        cur.execute(create_table_user)
        conn.commit()
        conn.close()
    except Error as e:
        print("Error on Sql", e)

class User:
    def createUser(self, userID,userName, password):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()

        creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO USER VALUES (?,?,?,?,null)", (userID, userName, password, creation_time))
        conn.commit()
        print("Created Successfully!")
    
    def deleteUser(self, userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        
        cur.execute("DELETE FROM USER WHERE userID == {userID, }")
        conn.commit()
        print("Deleted Successfully")

    @staticmethod
    def login(username, password):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * FROM USER WHERE password = '{ password, }' AND username = '{ username, }'")
        conn.commit()
        if cur.fetchone():
            return True
        else:
            return False
        conn.close()
    def updatePassword(userID, password):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("UPDATE USER SET password = self.password WHERE userID = '{userID, }'")
        conn.commit()
        return cur.fetchall()

    @staticmethod
    def soldItem(itemid, newUserID):
        result = Item.setBuyer(itemid, newUserID)
        if (result == False):
            return False
        return True

    @staticmethod
    def create_connection():
        conn = None
        try:
            conn = sqlite3.connect("chibaba.db")
            return conn
        except Error as e:
            print(e)

        return None

    def showUser(self,userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELETE * FROM USER")
        conn.commit()
        return cur.fetchall()

    def showItem_user(self, userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * from items where id = '{userID, }'")
        conn.commit()

        return cur.fetchall()

    @staticmethod
    def purchaseHistory(userID):
        conn = User.create_connection()
        if (conn is None):
            return None

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM items WHERE buyerID=?", (userID, ))
            result = [x for x in cur.fetchall()]

        return result, cur.description

    @staticmethod
    def sellingHistory(userID):
        conn = User.create_connection()
        if (conn is None):
            return None
        
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM items WHERE id=?", (userID, ))
            result = [x for x in cur.fetchall()]
        
        return result, cur.description

if __name__ == '__main__':
    create_db('chibaba.db')
    a = User()
    a.createUser(5161616, "Steven Shen", 990928)
