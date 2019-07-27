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
        create_table_transaction = """CREATE TABLE IF NOT EXISTS TRANSACTION_TABLE(
                                    transactionID integer primary key,
                                    buyerID text,
                                    sellerID text,
                                    price text,
                                    creation_time time
                                    -- userID integer references USER(userID)
                                    -- itemID real refereences ITEM(itemID),
                                ); """
        cur = conn.cursor()
        cur.execute(create_table_transaction)
        conn.commit()
        conn.close()
    except Error as e:
        print("Error on Sql", e)

class transaction:
    def __init__(self, buyerID, sellerID, price):
        self.buyerID = buyerID
        self.sellerID = sellerID
        # self.itemID = itemID
        self.price = price

    def createTransaction(self):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()

        self.transactionID = random.randint(1,999999);
        self.creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO TRANSACTION_TABLE VALUES (?,?,?,?,?)", (self.transactionID, self.buyerID, self.sellerID, self.price, self.creation_time))
        conn.commit()
        print("Created Successfully!")

    def showTransaction_id(self, transactionID):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * from TRANSACTION_TABLE where transactionID = self.transactionID")
        conn.commit()

    def showTransaction_user(self, userID):
        try:
            conn = sqlite3.connect('user.db')
        except Error as e:
            print(e)

        cur = conn.cursor()
        cur.execute("SELECT * from TRANSACTION_TABLE where userID = self.userID")
        conn.commit()


if __name__ == '__main__':
    create_db('user.db')
    a = transaction('buyer1', 'seller1', '$12')
    a.createTransaction()
