import sqlite3
from sqlite3 import Error
import json 

from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_restplus import inputs
from flask_restplus import reqparse


app = Flask(__name__)

@app.route('/items')
def returnItem():
    # item_id = request.json['item_id']

    try:
        conn = sqlite3.connect('chibaba.db')
    except Error as e:
        print("Error on Sql", e)

    cur = conn.cursor()

    cur.execute("SELECT * from items")
    conn.commit()
    result = cur.fetchall()

    items = []
    for row in result:
        print (row);
        items.append({'itemName': row[0], 'itemID': row[1], 'price': row[2], 'itemStatus': row[3], 'itemDescription': row[4], 'id':row[5]})
     
    conn.close()

    return (json.dumps(items))

if __name__ == '__main__':
    app.run(debug=True)

