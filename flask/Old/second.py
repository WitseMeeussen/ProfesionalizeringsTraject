from encodings import utf_8
from flask import Flask , request, jsonify
from flask_restful import Api, Resource
import pymongo
import bcrypt

import os
app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient('mongodb://db:27017')
db = client["SentencesDatabase"]
users = db["Users"]

def returnJson(status,message):
    return jsonify({
        "status":status,
        "message":message
    })

def verifyPW(username,password):
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    return bcrypt.checkpw(password.encode('utf8'), hashed_pw.encode('utf8'))



class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        users.insert_one({
            "Username":username,
            "Password": hashed_pw.decode('utf-8'),
            "Sentence":"",
            "Tokens":5
        })

        user = users.find({"Username":username})[0]
        return returnJson(200,user["Password"])

class Store(Resource):
    def post(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]
        sentence = data["sentence"]
        
        user = users.find({"Username":username})[0]

        
        if not verifyPW(username,password):
            return returnJson(302,"")

         
        num_tokens = user["Tokens"] -1
        if num_tokens <0:
            return returnJson(301,"No tokens left")

        users.update_one({
            "Username":username
        }, {
            "$set":{"Sentence":sentence,
            "Tokens":num_tokens}
        })

        return returnJson(200, "tokens left: "+ str(num_tokens))

class Get(Resource):
    def post(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]
        
        user = users.find({"Username":username})[0]

        
        if not verifyPW(username,password):
            return returnJson(302,"login failed")

         
        num_tokens = user["Tokens"] -1
        if num_tokens <0:
            return returnJson(301,"No tokens left")

        return returnJson(200, user["Sentence"])



api.add_resource(Register,"/register")
api.add_resource(Store,"/store")
api.add_resource(Get,"/get")

if __name__=="__main__":
    app.run(host='0.0.0.0')
