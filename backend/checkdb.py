import sqlite3

mydb = sqlite3.connect('chibaba.db')
cursor = mydb.cursor()

cursor.execute('select name from sqlite_master where type="table";')
tables = cursor.fetchall()
print(tables)

cursor.execute('select * from USER')
user_item = cursor.fetchall()
print(user_item)

cursor.execute('select * from TRANSACTION_TABLE')
trans = cursor.fetchall()
print(trans)
