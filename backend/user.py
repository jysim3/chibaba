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
                                        userID integer primary key AUTOINCREMENT,
                                        userName text NOT NULL UNIQUE,
                                        password text,
                                        creation_time time,
                                        score integer,
                                        item text references items(itemID)
                                    ); """
        cur = conn.cursor()
        cur.execute(create_table_user)
        conn.commit()
        conn.close()
    except Error as e:
        print("Error on Sql", e)


class User:
    @staticmethod
    def createUser(userName, password):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()

        creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO USER(userName,password,creation_time,item) VALUES (?,?,?,0,null)", (userName, password, creation_time))
        conn.commit()
        print("Created Successfully!")
        cur.execute("SELECT userID FROM USER WHERE userName = ?",(userName,))
        conn.commit()
        user_id = cur.fetchone()
        

        # conn.close()
        return True,user_id

    
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
        cur.execute(f"SELECT * FROM USER WHERE password = '{ password , }' AND username = '{ username , }'")
        conn.commit()
        k = cur.fetchone()
        print(k)
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
    def soldItem(itemid, buyerID):
        result = Item.setBuyer(itemid, buyerID)
        if (result == False):
            return False
        else:
            try:
                conn = sqlite3.connect('chibaba.db')
            except Error as e:
                print(e)
            cur = conn.cursor()
            cur.execute("SELECT id FROM item WHERE itemID = ?",(itemid,))
            conn.commit()
            sellerID = cur.fetchone()
            print(sellerID)
            cur.execute("UPDATE USER SET score = score + 1 WHERE userID = ?",(sellerID))
            conn.commit()
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

    def showUser(userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * FROM USER WHERE userID=?", (userID, ))
        result = [x for x in cur.fetchall()]
        # print(result)
        return result,cur.description


    def showItem_user(userID):
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
