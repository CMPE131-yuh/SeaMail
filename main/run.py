#imports for pymongo to connect application to external database through pymongo api
from dotenv import dotenv_values
from flask_pymongo import pymongo
from pymongo.mongo_client import MongoClient
from flask_socketio import SocketIO, emit
import gridfs

#import app object from init py file to be able to run the application
from src import myapp_obj

#config to be able to get uri and other information from .env file
config = dotenv_values(".env")

#uri link to connect to external mongo database
MONGO_URI = 'mongodb+srv://hanasuzuki:8gZpPyV7ZkTb7XOi@test.6mtzohb.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'

#socketio initialization to run with app object from init py
socketio = SocketIO(myapp_obj, cors_allowed_origins="*")

#connection to mongoDB client and connecting to each collection in the SeaMail databaase to intialize them as reusable objects
mongo = MongoClient(MONGO_URI) #initialize mongo client
db = mongo.get_database('SeaMail') #set variable db as the connection to the SeaMail mongoDB database
emails = pymongo.collection.Collection(db, 'emails') #connect to emails collection in the SeaMail database
todos = pymongo.collection.Collection(db, 'todolist') #connect to todos collection in the SeaMail database
users = pymongo.collection.Collection(db, 'users') #connect to users collection in the SeaMail database
chat_history = pymongo.collection.Collection(db, 'chat') #connect to chat_history collection in the SeaMail database
requests = pymongo.collection.Collection(db, 'request') #connect to requests collection in the SeaMail database
blocked = pymongo.collection.Collection(db, 'blocked') #connect to blocked collection in the SeaMail database
blockedEmails = pymongo.collection.Collection(db, 'blockedEmails') #connect to blockedEmails collection in the SeaMail database
image = pymongo.collection.Collection(db, 'images') #connect to image collection in the SeaMail database

#gridfs for file download
grid_fs = gridfs.GridFS(db)

#start application on localhost under socketio
if __name__ == '__main__':
    socketio.run(myapp_obj, debug = True) #run application with debug set to True for real time refreshing for development
