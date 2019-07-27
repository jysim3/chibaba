from flask import Flask, request, json, jsonify
from user import User

app = Flask(__name__)

@app.route("/purchaseItem", methods=['POST'])
def purchaseItem():
    inputJSON = request.get_json()
    itemID = inputJSON['itemID']
    userID = inputJSON['userID']
    if (itemID is None or userID is None):
        return jsonify(status=404)
    
    #Set item to be sold and make it belong to the user
    User.soldItem(itemID, userID)
    return jsonify(status=200)

@app.route("/login", methods=['POST']) 
def login():
    inputJSON = request.get_json()
    username = inputJSON['username']
    password = inputJSON['password']
    if User.login(username,password):
        return jsonify(status=200),200
    else:
        return jsonify(status=401),401


if __name__ == '__main__':
    app.run()
