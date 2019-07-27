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
        
        cur.execute("DELETE FROM USER WHERE userID == (?) ", userID)
        conn.commit()
        print("Deleted Successfully")

    def updatePassword(self,userID, password):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("UPDATE USER SET password = self.password WHERE userID == (?)", userID)
        conn.commit()
        print("Updated Successfully")

    def showUser(self,userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELETE * FROM USER")
        conn.commit()
        return cur.fatchall()

    def login(userID, password ):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELETE * FROM USER WHERE userID == (?) AND password == (?)", userID,password)
        conn.commit()
        return cur.fatchall()        

    def showItem_user(self, userID):
        try:
            conn = sqlite3.connect('chibaba.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * from items where id == ? ",userID)
        conn.commit()

        return cur.fetchall()


if __name__ == '__main__':
    create_db('chibaba.db')
    a = User()
    items = a.showItem_user(46833883)
    for item in items:
        print(item)