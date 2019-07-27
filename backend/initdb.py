import sqlite3
import random
import datetime,re
from sqlite3 import Error
from item import Item
conn = sqlite3.connect('chibaba.db')
cur = conn.cursor()


user_list = []
def create_user():
    user_list = [[11111111,'steven','123456'],[22222222,'yang','123456'],[333333333,'jie','123456'],[44444444,'cat','123456'],[55555555,'jack','123456'],[66666666,'izzy','123456'],[77777777,'micheal','123456'],[88888888,'matt','123456'],[99999999,'steven','123456']]

    for i in user_list:
        user = []
        for j in range(len(i)):
            user.append(i[j])
        creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user.append(creation_time)
        print(user)
        cur.execute("INSERT INTO USER VALUES (?,?,?,?,null)", user)
    conn.commit()
    print("Created Successfully!")


def create_item():
        #memes = Item("Memes", 123, 500, 0, "The end of the memes", None, 46833883)
    item_list = [["item1", 1, 50, 0, "The end of the memes", None, 11111111],["item2", 2, 50, 0, "The end of the memes", None, 11111111],["item3", 3, 50, 0, "The end of the memes", None, 33333333],["item4", 4, 50, 0, "The end of the memes", None, 22222222],\
                 ["item5", 5, 50, 0, "The end of the memes", None, 11111111],["item6", 6, 50, 0, "The end of the memes", None, 11111111],["item7", 7, 50, 0, "The end of the memes", None, 33333333],["item8", 8, 50, 0, "The end of the memes", None, 22222222],\
                 ["item9", 9, 50, 0, "The end of the memes", None, 22222222],["item10", 10, 50, 0, "The end of the memes", None, 22222222],["item11", 11, 50, 0, "The end of the memes", None, 11111111],["item12", 12, 50, 0, "The end of the memes", None, 11111111]]

    for i in item_list:
        Item(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    conn.commit()

    print("Created Successfully!")


create_user()
create_item()

