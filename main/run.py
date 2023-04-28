#turn on application with debug on using flask
from dotenv import dotenv_values
from flask_pymongo import pymongo
from pymongo.mongo_client import MongoClient

from src import myapp_obj

config = dotenv_values(".env")

MONGO_URI = 'mongodb+srv://seamail:seamailpassword@cluster0.lct6aap.mongodb.net/?retryWrites=true&w=majority'

mongo = MongoClient(MONGO_URI)
db = mongo.get_database('SeaMail')
emails = pymongo.collection.Collection(db, 'emails')
todos = pymongo.collection.Collection(db, 'todolist')
users = pymongo.collection.Collection(db, 'users')

if __name__ == '__main__':
    myapp_obj.run(debug = True)