from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request
from fabric.api import *

application = Flask(__name__)

client = MongoClient('localhost:27017')
db = client.MachineData



@application.route('/')
def showIndex():
    return render_template('index.hbs')



if __name__ == "__main__":
    application.run(host='0.0.0.0')

