import os
import random
import sqlite3
from sqlite3 import Error
import json 
import datetime,re

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        create_table_user = """CREATE TABLE IF NOT EXISTS USER(
                                        userID integer primary key,
                                        userName text,
                                        password text,
                                        creation_time time,
                                        item text references items(itemid)
                                        -- points integer
                                    ); """
        cur = conn.cursor()
        cur.execute(create_table_user)
        conn.commit()
        conn.close()
    except Error as e:
        print("Error on Sql", e)

class User:
    def __init__(self, userID,userName, password):
        self.userID = userID
        self.userName = userName
        self.password = password

    def createUser(self):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()

        self.creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO USER VALUES (?,?,?,?)", (self.userID, self.userName, self.password, self.creation_time))
        conn.commit()
        print("Created Successfully!")
    
    def deleteUser(self, userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        
        cur.execute(f"DELETE FROM USER WHERE userID == self.userID")
        conn.commit()
        print("Deleted Successfully")

    def updatePassword(self,userID, password):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"UPDATE USER SET password = self.password WHERE userID = self.userID;")
        conn.commit()
        print("Updated Successfully")

    def showUser(self,userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"SELETE * FROM USER")
        conn.commit()

    def showItem_user(self, userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * from item where userID = self.userID")
        conn.commit()


if __name__ == '__main__':
    create_db('chibaba.db')
    a = User('046833333','abc', 123)
    a.createUser()


