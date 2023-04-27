#turn on application with debug on using flask
from src import myapp_obj

#connection to database
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

app = FastAPI()

myapp_obj.run(debug=True)