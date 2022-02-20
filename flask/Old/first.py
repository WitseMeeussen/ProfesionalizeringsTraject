from flask import Flask , request, jsonify
from flask_restful import Api, Resource
import pymongo

import os
app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient('mongodb://db:27017')
db = client["newDB"]
UserNum = db["UserNum"]
json = {
    'num_of_users':0
}
#insert_one for one insert_many for more
db.UserNum.insert_one(json)



def checkInputData(postedData,functionName):
    if (functionName == "devide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]["num_of_users"] +1
        UserNum.update({},{"$set":{"num_of_users":prev_num}})
        return str("Helo user "+ str(prev_num))   
    def post(self):

        postedData = request.get_json()
        x = int(postedData["x"])
        y = int(postedData["y"])


        retJson = {
            "message": x+y,
            "status":200
        }
        
        #post function
        return jsonify(retJson)

class Subtract(Resource):
    def post(self):
        postedData = request.get_json()
        x = int(postedData["x"])
        y = int(postedData["y"])

        retJson = {
            'message': x-y,
            'status':200
        }
        
        #post function
        return jsonify(retJson)

class Multiply(Resource):
    def post(self):
        postedData = request.get_json()
        x = int(postedData["x"])
        y = int(postedData["y"])

        retJson = {
            'message': x*y,
            'status':200
        }
        
        #post function
        return jsonify(retJson)

class Devide(Resource):
    def post(self):
        postedData = request.get_json()
        x = int(postedData["x"])
        y = int(postedData["y"])

        retJson = {
            'message': x/y,
            'status':200
        }
        
        #post function
        return jsonify(retJson)

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]["num_of_users"] +1
        UserNum.update({},{"$set":{"num_of_users":prev_num}})
        return str("Helo user "+ str(prev_num))       

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/substract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Devide,"/devide")
api.add_resource(Visit,"/visit")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(host='0.0.0.0')
