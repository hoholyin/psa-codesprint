from db import *
from flask import Flask, jsonify, request, make_response, url_for
import os
import sys
import pymongo
import json
from bson import json_util

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/submitdata", methods=['POST'])
def submitdata():
    try:
        formData = request.get_json()
        #extract various fields from form
        name = formData["name"]
        contact = formData["contact"]
        email = formData["email"]
        department = formData["department"]
        db.employeeData.insert_one({
            "name": name,
            "contact": contact,
            "email": email,
            "department": department
        })
    except:
        return jsonify({'message': 'error encountered'}), 500
    return jsonify({'message': 'data submitted successfully'}), 200

@app.route("/submitscore", methods=['POST'])
def submitscore():
    try:
        formData = request.get_json()
        #extract various fields from form
        name = formData["name"]
        scores = formData["scores"]
        db.employeeScore.insert_one({
            "name": name,
            "scores": scores
        })
    except:
        return jsonify({'message': 'error encountered'}), 500
    return jsonify({'message': 'data submitted successfully'}), 200

@app.route("/submitrating", methods=['POST'])
def submitrating():
    formData = request.get_json()
    if not db.employeeScore.find_one({'name': formData['name']}):
        return jsonify({'message': 'user not found'}), 501
    db.employeeScore.update({'name': formData['name']}, {
                            '$set': {
                                'rating': formData['rating']
                                }
                            }, upsert=True)
    return jsonify({'message': 'data submitted successfully'}), 200

@app.route("/getrating", methods=['GET'])
def getrating():
    result = [json.loads(json.dumps(doc, default=json_util.default)) for doc in db.employeeScore.find({}, {"_id": 0, "name": 1, "rating": 1})]
    return jsonify({'result': result}), 200

@app.route("/getallscore", methods=['GET'])
def getallscore():
    allEmployeeData = [json.loads(json.dumps(doc, default=json_util.default)) for doc in db.employeeData.find({})] #return everything 
    allEmployeeScore = [json.loads(json.dumps(doc, default=json_util.default)) for doc in db.employeeScore.find({})] #return everything
    if (not allEmployeeData or not allEmployeeScore):
        return jsonify({"message": 'data not found'}), 500
    else:
        return jsonify({'allEmployeeData': allEmployeeData, 'allEmployeeScore': allEmployeeScore}), 200    

@app.route("/getscorebyname", methods=['GET'])
def getscorebyname():
    name = request.args.get('name')
    employeeDataResult = db.employeeData.find_one({
        'name': name
    })
    employeeScoreResult = db.employeeScore.find_one({
        'name': name
    })
    if (not employeeDataResult or not employeeScoreResult):
        return jsonify({"message": 'data not found'}), 500
    else:
        return jsonify({'employeeData': employeeDataResult, 'employeeScore': employeeScoreResult}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)