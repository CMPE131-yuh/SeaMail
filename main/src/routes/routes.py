#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import Flask, render_template, redirect, escape, Request

#import fastapi for db communication
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

#import backend models for CRUD and database
from src.models.models import Email, EmailUpdate

#renaming APIRouter to router for abstraction
router = APIRouter()

#render index route
@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    return render_template('index.html')

#create request, make an email
@router.post("/", response_description="Create a new email", status_code=status.HTTP_201_CREATED, response_model=Email)
def create_email(request: Request, email: Email = Body(...)):
    email = jsonable_encoder(email)
    new_email = request.app.database["SeaMail.emails"].insert_one(email)
    created_email = request.database["SeaMail.emails"].find_one(
        {"_id": new_email.inserted_id}
    )
    return created_email

#post request, grab list of mail
@myapp_obj.route("/mailroom")
@myapp_obj.route("/mailroom.html")
@router.get("/mailroom", response_description="List All Emails", response_model=List[Email])
def list_emails(request: Request):
    emails = list(request.app.database["SeaMail.emails"].find(limit=100))
    #return render_template('mailroom.html', emails = emails)
    return emails