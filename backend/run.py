from flask import Flask, request, json, jsonify
from user import User
from item import Item
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/purchaseItem", methods=['POST'])
def purchaseItem():
    inputJSON = request.get_json()
    itemID = inputJSON['itemID']
    userID = inputJSON['userID']
    if (itemID is None or userID is None):
        return jsonify(status=404)
    
    #Set item to be sold and make it belong to the buyer
    User.soldItem(itemID, userID)
    return jsonify(status=200)

@app.route("/login", methods=['POST']) 
def login():
    inputJSON = request.get_json()
    print("input == ", inputJSON)
    username = inputJSON['username']
    password = inputJSON['password']
    if User.login(username,password):
        return jsonify(status=200),200
    else:
        return jsonify(status=401),401

@app.route("/sellItem", methods=['POST'])
def sellItem():
    inputJSON = request.get_json()
    #FIXME: CHange this later on, change to whatever the latest ID + 1
    itemID = inputJSON['itemID']
    name = inputJSON['name']
    price = inputJSON['price']
    status = 1
    description = inputJSON['description']
    sellerID = inputJSON['userID']

    itemToSell = Item.addItems(name, itemID, price, status, description, None, sellerID)
    if (itemToSell == False):
        return jsonify(status=404)
    
    return jsonify(status=200)

if __name__ == '__main__':
    app.run()
