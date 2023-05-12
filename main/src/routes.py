#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import render_template, request, redirect, url_for, session
from flask_socketio import send
from bson.objectid import ObjectId
from bson import Binary
from PIL import Image
import matplotlib.pyplot as plt

import io

from run import emails, todos, users, socketio

myapp_obj.secret_key = "SEAMAIL.HQ"


#render index route
@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/index.html", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#add emails to database
@myapp_obj.route('/sendMail', methods=['GET', 'POST'])
def sendEmail():
    if request.method == 'POST':
        #if(users.find({'username': session['user'], 'blocked': True})):
        #    sub = request.form['sub']
        #    msg = request.form['msg']
        #    rec = request.form['recipe']
        #    blocked.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False})
        sub = request.form['sub']
        msg = request.form['msg']
        rec = request.form['recipe']
        if request.files:
            emailImage = request.files['image']
            emails.save_file(emailImage.filename, emailImage)
            emails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'img': emailImage, 'hasImg': True})
        else:
            emails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'hasImg': False})
        return redirect(url_for('listEmails'))
    else:
        return render_template('mailroom.html', message='message not sent', current_user = session['user'])

#open image that was sent from email
@myapp_obj.route('/openImage/<oid>', methods=['GET', 'POST'])
def openImage(oid):
    if request.method == 'POST':
        #if emails.find({'_id': ObjectId(oid), 'hasImg': True}).count() > 0:
        image = emails.find({'_id': ObjectId(oid)})
        return render_template('viewImage.html', view=image)
        #else:
        #return render_template('viewImage.html', view='No Image Attached')

#list emails from database
@myapp_obj.route('/mailroom', methods=['GET', 'POST'])
def listEmails():
    if emails.find({'username': session['user']}).count() > 0:
        maillist = emails.find({'username': session['user']})
        return render_template('mailroom.html', emails=maillist, current_user = session['user'])
    else:
        return render_template('mailroom.html', message='No Emails At This Time', current_user = session['user'])

#list outbox emails from database
@myapp_obj.route('/outbox', methods=['GET', 'POST'])
def listOutbox():
    maillist = emails.find({'delete': False})
    return render_template('outbox.html', sent=maillist, current_user = session['user'])

#unsend emails for both sender and receiver
@myapp_obj.route('/unsendEmail/<oid>', methods=['GET', 'POST'])
def unsendEmail(oid):
    if request.method == 'POST':
        emails.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}})
        emails.delete_one({'delete': True})
        return redirect(url_for('listOutbox'))
    return render_template('outbox.html', sent='Error Loading Outbox')

#delete email for the current user's mailroom
@myapp_obj.route('/delEmail/<oid>', methods=['GET', 'POST'])
def delEmail(oid):
    if request.method == 'POST':
        emails.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}})
        emails.delete_one({'delete': True})
        return redirect(url_for('listEmails'))
    return render_template('mailroom.html', emails='Error Loading Mailroom')

#render todolist
@myapp_obj.route('/todolist', methods=['GET', 'POST'])
def todo():
    todolist = todos.find({'username': session['user']})
    return render_template('todo.html', todos=todolist, username=session['user'])

#add item to todo list database
@myapp_obj.route('/addtodo', methods=['GET', 'POST'])
def addTodo():
    if request.method == 'POST':
        todoitem = request.form['todoitem']
        todos.insert_one({'username': session['user'], 'item': todoitem, 'delete': False})
        getTodoItem = todos.find({'username': session['user']})
        return redirect(url_for('todo'))
    return render_template('todo.html', todos='Todo Not Rendered')

#remove item from todo list database collection
@myapp_obj.route('/removetodo/<oid>', methods=['GET', 'POST'])
def remTodo(oid):
    if request.method == 'POST':
        todos.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}})
        todos.delete_one({'delete': True})
        return redirect(url_for('todo'))
    return render_template('todo.html', todos='Todo Not Rendered')

#logout funcionality, logs out current user session
@myapp_obj.route('/logout', methods = ['GET', 'POST'])
def logout():
    delete_user = session['user']
    print(delete_user)
    if request.method == 'POST':
        if 'logout_button' in request.form:
            session.pop('user')
            return redirect(url_for('afterLogout'))
        elif 'delete_button' in request.form:
            users.delete_one({'username':delete_user})
            session.pop('user')
            return redirect(url_for('login'))
    return render_template('logout.html', current_user = session['user'])

#login into user account, redirect into user mailroom
@myapp_obj.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        psw = request.form['password']
        if users.find_one({'username':name, 'password':psw}) != None:
            session['user'] = name
            return redirect(url_for('listEmails'))
        else:
            return """
            <div align = "center">
                <h3>No account match found</h3>
                </br>
                <a href = 'login'>Return to login page</a>
            </div>
             """
    return render_template('log_in.html')

#register new user
@myapp_obj.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['username']
        new_user_password = request.form['password']
        new_user_email = request.form['email']
        new_user = {'username' : new_username, 'password' : new_user_password, 'email' : new_user_email, 'blocked': False}
        if users.find_one({'username': new_username}) == None:
            users.insert_one(new_user)
            session['user'] = new_username
            return redirect(url_for('login'))

        return """
        <h3>That username already exists!</h3>
        </br>
        <a href = "register">Return to register page</a>
        """
    return render_template('register.html')

#logged out rendering after logging out
@myapp_obj.route('/afterLogout')
def afterLogout():
    return render_template('logged_out.html')

#---------------------------------------------------------
#socket message rouonte
@socketio.on('message')
def handle_message(message):
    #emit('message', json_data, broadcast=True, include_self=False)
    print("Received Message: " + message)
    if message != "User Connected!":
        send(message, broadcast=True)

#render messagenger route
@myapp_obj.route('/message-room', methods=['GET', 'POST'])
def messageRoom():
    return render_template('message.html')
#---------------------------------------------------------
