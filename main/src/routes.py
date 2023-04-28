#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import render_template, request

from run import mongo, emails

mailing = mongo.db.emails

#render index route
@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/index.html", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#add emails to database
@myapp_obj.route('/sendMail', methods=['GET', 'POST'])
def addEmail():
    if request.method == 'POST':
        mailing.insert_one({'sender': 'test sender', 'subject': 'test subject', 'message': 'test message'})
        return render_template('mailroom.html', message='message sent')
    else:
        return render_template('mailroom.html', message='message not sent')

#list emails from database
@myapp_obj.route('/mailroom', methods=['GET', 'POST'])
def listEmails():
    if request.method == 'POST':
        maillist = mailing.find()
        return render_template('mailroom.html', emails=maillist)
    else:
        return render_template('mailroom.html', message='Email List not listed')