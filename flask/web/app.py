from encodings import utf_8
import json
from flask import Flask , request, jsonify
from flask_restful import Api, Resource
import pymongo
import bcrypt

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import os
app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient('mongodb://db:27017')
db = client["SentencesDatabase"]
users = db["Users1"]

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

def isUsername(username):
    return users.count_documents({"Username":username}) > 0

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        if isUsername(username):
            return returnJson(301,username + " , this username already exist")

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        users.insert_one({
            "Username":username,
            "Password": hashed_pw.decode('utf-8'),
            "Tokens":6
        })

        user = users.find({"Username":username})[0]
        return returnJson(200,"succesful signed up: "+username)

class Detect(Resource):
    def post(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]
        text1 = data["text1"]
        text2 = data["text2"]

        if not isUsername(username):
            return returnJson(302,username + " , this username does not exist")

        if not verifyPW(username,password):
            return returnJson(303, "wrong password")

        tokens = users.find({"Username":username})[0]["Tokens"]

        if tokens == 0: return returnJson(304 , "Out of tokens")

        nlp = spacy.load('en_core_web_sm')

        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)

        retJson = {
            "status":200,
            "similarity":ratio
        }

        users.update({
            "Username": username
        }, {
            "$set":{
                "Tokens": tokens -1
            }
        })

        return jsonify(retJson)


api.add_resource(Register,"/register")
api.add_resource(Detect,"/detect")

if __name__=="__main__":
    app.run(host='0.0.0.0')
