#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import render_template, request, redirect, url_for, session, flash
from flask_socketio import send
from bson.objectid import ObjectId
from bson import Binary
from PIL import Image
import matplotlib.pyplot as plt
import codecs

import io
import random
from string import ascii_uppercase

from run import emails, todos, users, chat_history, roomz, grid_fs, blocked, blockedEmails

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
        sub = request.form['sub']
        msg = request.form['msg']
        rec = request.form['recipe']
        if blocked.count_documents({'username': rec, 'userBlock': session['user']}) != 0:
            blockedEmails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'notify': True})
            flash("This User Has Blocked You")
            return redirect(url_for('listEmails'))
        #if request.files:
        #    emailImage = request.files['image']
        #    image = grid_fs.put(emailImage, content_type = pimage.content_type)
        #    emails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'img': image, 'hasImg': True})
        else:
            emails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'hasImg': False, 'notify': True})
            return redirect(url_for('listEmails'))
    else:
        return render_template('mailroom.html', message='message not sent', current_user = session['user'])

#open image that was sent from email
@myapp_obj.route('/openImage/<oid>', methods=['GET', 'POST'])
def openImage(oid):
    if request.method == 'POST':
        item = emails.find_one({'_id': oid})
        image = grid_fs.get(item['_id'])
        base64_data = codecs.encode(image.read(), 'base64')
        image = base64_data.decode('utf-8')
        return render_template('viewImage.html', image = image)
    
#list emails from database
@myapp_obj.route('/mailroom', methods=['GET', 'POST'])
def listEmails():
    if request.method == 'GET':
        maillist = emails.find({'username': session['user']})
        if(emails.count_documents({'username': session['user'], 'notify': True}) != 0):
            flash("You Got Mail!")
            return render_template('mailroom.html', emails=maillist, current_user = session['user'])
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

@myapp_obj.route('/change_password', methods = ['GET', 'POST'])
def changePassword():
    if request.method == 'POST':
        check_username = users.find_one({'username' : request.form['username'], 'password' : request.form['current_password']})
        check_email = users.find_one({'email' : request.form['username'], 'password' : request.form['current_password']})
        new = request.form['new_password']

        if check_email == None and check_username == None:
            return """
            <div align='center'>
                <h3>Wrong combination of username/email and password</h3>
                <h3>Please try again!</h3>
                </br>
                <a href = "change_password">Return to the previous page</a>
            </div>
            """
        elif request.form['current_password'] != request.form['check_current']:
            return """
            <h3>The passwords don't match!</h3>
            </br>
            <a href = "change_password">Return to the previous page</a>
            """
        else:
            query = {'username' : request.form['username']}
            update = { "$set": { "password": new } }
            users.update_one(query, update)
            return redirect(url_for('logout'))

    return render_template('password_change.html')

@myapp_obj.route('/enterance', methods = ['GET', 'POST'])
def enterance():
    if request.method == 'POST':
        recipient = request.form['recipient']
        list = chat_history.find({'$or': [{'$and' : [{'recipient' : recipient, 'sender':session['user']}]},{'$and' : [{'recipient' : session['user'], 'sender' : recipient}]}]})
        num = chat_history.find({'$or': [{'$and' : [{'recipient' : recipient, 'sender':session['user']}]},{'$and' : [{'recipient' : session['user'], 'sender' : recipient}]}]}).count()

        if num == None:
            request.insert_one({True: session['user'], False : recipient})
            return """
            <div align='center'>
                <h3>Chat request has been sent successfully to {{recipient}}</h3>
                <h3>Please wait for them to accept the request!</h3>
                </br>
                <a href = "enterance">Return to the previous page</a>
            </div>
            """
        else:
            session['num'] = num
            session['recipient'] = recipient
            return redirect(url_for('room', chats = list))

    return render_template('enterance.html')

@myapp_obj.route('/room', methods = ['GET', 'POST'])
def room():
    list = chat_history.find({'$or': [{'$and' : [{'recipient' : session['recipient'], 'sender':session['user']}]},{'$and' : [{'recipient' : session['user'], 'sender' : session['recipient']}]}]})

    if request.method == 'GET':
        return render_template('room.html', chats = list)
    num_message = chat_history.find({'$or': [{'$and' : [{'recipient' : session['recipient'], 'sender':session['user']}]},{'$and' : [{'recipient' : session['user'], 'sender' : session['recipient']}]}]}).count()
    if session['num'] != num_message:
        session['num'] = num_message
        return render_template('room.html', chats = list)

    if request.method == 'POST':
        if 'exit' in request.form:
            session.pop('recipient')
            session.pop('num')
            return redirect(url_for('enterance'))

        new_msg = request.form['message']
        chat_history.insert_one({'sender' : session['user'], 'recipient' : session['recipient'], 'message' : new_msg})
        list = chat_history.find({'$or': [{'$and' : [{'recipient' : session['recipient'], 'sender':session['user']}]},
        {'$and' : [{'recipient' : session['user'], 'sender' : session['recipient']}]}]})
        session['num'] = chat_history.find({'$or': [{'$and' : [{'recipient' : session['recipient'], 'sender':session['user']}]},
        {'$and' : [{'recipient' : session['user'], 'sender' : session['recipient']}]}]}).count()
        return render_template('room.html', chats = list)
    
    

    return render_template('room.html', chats = list)

#render user lists
@myapp_obj.route('/accounts', methods=['GET', 'POST'])
def listAccounts():
    userList = users.find()
    return render_template('blockedList.html', users = userList)
#add user to current user's blocked user emails
@myapp_obj.route('/block/<oid>', methods = ['GET', 'POST'])
def block(oid):
    if request.method == 'POST':
        userBlocked = users.find_one({'_id': ObjectId(oid)})
        if userBlocked:
            nameBlocked = userBlocked['username']
            blocked.insert_one({'username': session['user'], 'userBlock': nameBlocked})
            flash("User Blocked")
            return redirect(url_for('listAccounts'))
    
#remove user from current user's blocked user emails
@myapp_obj.route('/unblock/<oid>', methods = ['GET', 'POST'])
def unblock(oid):
    if request.method == 'POST':
        userBlocked = users.find_one({'_id': ObjectId(oid)})
        if userBlocked:
            nameUnblocked = userBlocked['username']
            blocked.delete_one({'_id': ObjectId(oid)})
            if blockedEmails.count_documents({'sender': nameUnblocked}) != 0:
                blockedEmail = blockedEmails.find_one({'sender': nameUnblocked})
                emails.insert_one(blockedEmail)
        flash("User Unblocked")
        return redirect(url_for('listAccounts'))