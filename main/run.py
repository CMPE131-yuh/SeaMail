#turn on application with debug on using flask
from src import myapp_obj

#connection to database
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from src.routes import router as db_route

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config("ATLAS_URI"))
    app.database = app.mongodb_client[config["clientDB"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(db_route, tags=["mailroom"], prefix="/mailroom")

myapp_obj.run(debug=True)