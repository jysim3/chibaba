import os
import random
import sqlite3
from sqlite3 import Error
# import requests
import json 
import datetime,re

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        create_table_user = """CREATE TABLE IF NOT EXISTS USER(
                                        userID integer primary key,
                                        userName text,
                                        password text,
                                        creation_time time
                                        -- item text,
                                        -- points integer
                                    ); """
        cur = conn.cursor()
        cur.execute(create_table_user)
        print("hihihihihihihi")
        conn.commit()
        conn.close()
    except Error as e:
        print("Error on Sql", e)

class User:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def createUser(self):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()

        self.userID = random.randint(1,999999);
        print(self.userID)
        self.creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO USER VALUES (?,?,?,?)", (self.userID, self.userName, self.password, self.creation_time))
        conn.commit()
        print("Created Successfully!")
    
    def deleteUser(self, userID):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        
        cur.execute(f"DELETE FROM USER WHERE userID == self.userID")
        conn.commit()
        print("Deleted Successfully")

    def updatePassword(self,userID, password):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"UPDATE USER SET password = self.password WHERE userID = self.userID;")
        conn.commit()
        print("Updated Successfully")

    def showUser(self,userID):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute(f"SELETE * FROM USER")
        conn.commit()


if __name__ == '__main__':
    create_db('user.db')
    a = User('abc', 123)
    a.createUser()


