from db import *
from flask import Flask, jsonify, request, make_response, url_for
import os
import sys
import pymongo

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/submit", methods=['POST'])
def submit():
    formData = request.get_json()
    #extract various fields from form
    name = formData["name"]
    field1 = formData["field1"]
    #and so on...
    db.employeeData.insert_one({
        #"userID": userID,
        "name": name,
        "field1": field1
    })
    return jsonify({'message': 'data submitted successfully'}), 200

@app.route("/getscore", methods=['GET'])
def getscore():
    name = request.args.get('name')
    result = db.employeeScore.find_one({
        'name': name
    })
    if not result:
        return jsonify({"message": 'data not found'}), 500
    else:
        return jsonify({'result': result["score"]}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)