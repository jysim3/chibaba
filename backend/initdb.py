import sqlite3
import random
import datetime,re
from sqlite3 import Error
from item import Item
from user import create_db
conn = sqlite3.connect('chibaba.db')
cur = conn.cursor()

create_db('chibaba.db')

user_list = []
def create_user():
    user_list = [[5153884,'Shangjie','123456'],[1234567,'Yang','123456'],[23456789,'Steven','123456'],[3456789,'Cat','123456'],[45678901,'Andrew','123456'],[56789012,'Ravija','123456'],[67890123,'Harrison','123456'],[78901234,'Matt','123456'],[89012345,'Izzy','123456']]

    for i in user_list:
        user = []
        for j in range(len(i)):
            user.append(i[j])
        creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user.append(creation_time)
        print(user)
        cur.execute("INSERT INTO USER VALUES (?,?,?,?,0,null)", user)
    conn.commit()
    print("Created Successfully!")


def create_item():

    item_list = [["chocolate cake", 0, 0, "Fresh chocolate cake", None, 5153884],["chocolate milk", 0, 0, "Hot chocolate", None, 1234567],["burger", 0, 0, "beef burger", None, 23456789],["BBQ", 0, 0, "Australian BBQ on Wednesday", None, 45678901],\
                 ["Chinese Food", 0, 0, "The end of the memes", None, 5153884],["Thai Food", 0, 0, "The end of the memes", None, 56789012],["Old iphone", 0, 0, "Can use but slow", None, 33333333],["Hoodies", 0, 0, "Weared few times", None, 89012345],\
                 ["Fridge", 0, 0, "5 years", None, 45678901],["computer", 0, 0, "10 years ago", None, 67890123],["noodle", 50, 0, "asian noodle pretty ", None, 78901234],["cutlery", 0, 0, "don't perfect but can still use", None, 56789012]]

    for i in item_list:
        Item(i[0],i[1],i[2],i[3],i[4],i[5])
    conn.commit()

    print("Created Successfully!")


create_user()
create_item()

