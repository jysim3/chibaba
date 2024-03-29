#!/usr/bin/python3 
import sqlite3
from flask import Flask, request, json, jsonify
from user import User
from item import Item
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/items")
def returnItem():
    result, title = Item.getAllItems()
    items = []
    for row in result:
        item = dict()
        #print(row)
        for idx, column in enumerate(row):
            item[title[idx][0]] = row[idx]

        items.append(item)

    return jsonify(items)

@app.route("/selling")
def sellingItems():
    result, title = Item.getAllItemsOnSale()
    items = []
    for row in result:
        item = dict()
        #print(row)
        for idx, column in enumerate(row):
            item[title[idx][0]] = row[idx]

        items.append(item)

    return jsonify(items)

@app.route("/purchaseItems", methods=['POST'])
def purchaseItem():
    inputJSON = request.get_json()
    print(inputJSON)
    itemID = str(inputJSON['itemID'])
    userID = str(inputJSON['userID'])
    print(itemID + userID)
    if (itemID is None or userID is None):
        return jsonify(status=404)
    
    #Set item to be sold and make it belong to the buyer
    if User.soldItem(itemID, userID):
        return jsonify(status=200)
    else: 
        return jsonify(status=400)

@app.route("/login", methods=['POST']) 
def login():
    inputJSON = request.get_json()
    print("input == ", inputJSON)
    username = inputJSON['username']
    password = inputJSON['password']
    userID = User.login(username,password)
    if userID:
        return jsonify(userID=userID,status=200),200
    else:
        return jsonify(status=401),401

@app.route("/register", methods=['POST']) 
def register():
    inputJSON = request.get_json()
    print("input == ", inputJSON)
    username = inputJSON['username']
    password = inputJSON['password']

    result, userID = User.createUser(username, password)

    if result:
        return jsonify(userID),200
    else:
        return jsonify(status=401),401

@app.route("/getusrInfo", methods=['POST'])
def getusrInfo():
    inputJSON = request.get_json()
    print("input == ", inputJSON)
    userid = inputJSON['userID']
    result,title = User.showUser(userid)
    users = []
    for row in result:
        user = dict()
        for idx, column in enumerate(row):
            user[title[idx][0]] = row[idx]
        users.append(user)
        return jsonify(users),200
    else:
        return jsonify(status=401),401


@app.route("/sellItem", methods=['POST'])
def sellItem():
    inputJSON = request.get_json()
    #FIXME: CHange this later on, change to whatever the latest ID + 1
    name = inputJSON['name']
    price = inputJSON['price']
    status = 1
    description = inputJSON['description']
    sellerID = inputJSON['userID']
    image = inputJSON['image']

    itemToSell = Item.addItems(name, price, status, description, image, sellerID)
    if (itemToSell is None):
        return jsonify(status=404)

    return jsonify(status=200, itemID=itemToSell)

@app.route("/purchaseHistory", methods=['POST'])
def getPurchaseHistory():
    inputJSON = request.get_json()
    print(inputJSON)
    userID = inputJSON['userID']
    result, title = User.purchaseHistory(userID)
    items = []
    for row in result:
        item = dict()
        print(row)
        for idx, column in enumerate(row):
            item[title[idx][0]] = row[idx]

        items.append(item)

    return jsonify(items)

@app.route("/sellingHistory", methods=['POST'])
def getSellingHistory():
    inputJSON = request.get_json()
    userID = inputJSON['userID']
    result, title = User.sellingHistory(userID)
    items = []
    for row in result:
        item = dict()
        print(row)
        for idx, column in enumerate(row):
            item[title[idx][0]] = row[idx]

        items.append(item)

    return jsonify(items)

@app.route("/search", methods=['POST'])
def search():
    inputJSON = request.get_json()
    textString = inputJSON['input']
    result, title = Item.searchString(textString)
    items = []
    for row in result:
        item = dict()
        print(row)
        for idx, column in enumerate(row):
            item[title[idx][0]] = row[idx]

        items.append(item)

    return jsonify(items)

    return jsonify(searchResult)   

if __name__ == '__main__':
    app.run(debug=True)
