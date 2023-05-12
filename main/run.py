#turn on application with debug on using flask
from dotenv import dotenv_values
from flask_pymongo import pymongo
from pymongo.mongo_client import MongoClient
from flask_socketio import SocketIO, emit
import gridfs

from src import myapp_obj

config = dotenv_values(".env")

MONGO_URI = 'mongodb+srv://hanasuzuki:8gZpPyV7ZkTb7XOi@test.6mtzohb.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'

socketio = SocketIO(myapp_obj, cors_allowed_origins="*")

mongo = MongoClient(MONGO_URI)
db = mongo.get_database('SeaMail')
emails = pymongo.collection.Collection(db, 'emails')
todos = pymongo.collection.Collection(db, 'todolist')
users = pymongo.collection.Collection(db, 'users')
chat_history = pymongo.collection.Collection(db, 'chat')
roomz = pymongo.collection.Collection(db, 'roomz')
blocked = pymongo.collection.Collection(db, 'blocked')
blockedEmails = pymongo.collection.Collection(db, 'blockedEmails')

grid_fs = gridfs.GridFS(db)

if __name__ == '__main__':
    socketio.run(myapp_obj, debug = True, host='10.250.68.86', port=5000)