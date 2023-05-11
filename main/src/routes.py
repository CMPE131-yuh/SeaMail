#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import render_template, request, redirect, url_for, session
from run import emails, todos, users, socketio, chat_history, roomz
from flask_socketio import join_room, leave_room, send, emit
import random
from string import ascii_uppercase
from bson.objectid import ObjectId

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
        emails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg})
        return redirect(url_for('listEmails'))
    else:
        return render_template('mailroom.html', message='message not sent', current_user = session['user'])

#list emails from database
@myapp_obj.route('/mailroom', methods=['GET', 'POST'])
def listEmails():
    maillist = emails.find({'username': session['user']})
    return render_template('mailroom.html', emails=maillist, current_user = session['user'])

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
        return render_template('todo.html', todos=getTodoItem, username=session['user'])
    return render_template('todo.html', todos='Todo Not Rendered')

#remove item from todo list database collection
@myapp_obj.route('/removetodo/<oid>', methods=['GET', 'POST'])
def remTodo(oid):
    if request.method == 'POST':
        todos.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}})
        todos.delete_one({'delete': True})
        getTodoItem = todos.find({'username': session['user']})
        return render_template('todo.html', todos=getTodoItem, username=session['user'])
    return render_template('todo.html', todos='Todo Not Rendered')

@myapp_obj.route('/logout', methods = ['GET', 'POST'])
def logout():
    delete_user = session['user']
    if request.method == 'POST':
        if 'logout_button' in request.form:
            session.pop('user')
            return redirect(url_for('afterLogout'))
        elif 'delete_button' in request.form:
            users.delete_one({'username':delete_user})
            session.pop('user')
            return redirect(url_for('login'))
        elif 'change_password' in request.form:
            return redirect(url_for('changePassword'))
        elif 'change_name' in request.form:
            return redirect(url_for('changeName'))
    return render_template('logout.html', current_user = session['user'])

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

@myapp_obj.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['username']
        new_user_password = request.form['password']
        new_user_email = request.form['email'] + '@seamail.com'
        new_user = users(new_username, new_user_password, new_user_email)
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

@myapp_obj.route('/chatroom', methods = ['GET', 'POST'])
def chatroom():
    if request.method == 'POST':
        if 'create_room' in request.form:
            session['room'] = generate_unique_code(4)
            roomz.insert_one({'code':session['room']})
            session['recipient'] = request.form['recipient']
            new_chat = {'room_num' : session['room'], 'recipient' : session['recipient'], 'sender' : session['user'], 'chats' : ['hi']}
            chat_history.insert_one(new_chat)
        elif 'enter_room' in request.form:
            session['room'] = request.form['room_number']
            session['recipient'] = request.form['recipient']
        return redirect(url_for('room'))

    return render_template('chatroom.html')

@myapp_obj.route('/room', methods = ['GET', 'POST'])
def room():
    username = request.args.get('username')
    room = session['room']
    return render_template('room.html', username=username, room=room)


#Socket.io commands ---------------------------------------------------------------------------------------------------------------------
@socketio.on('send_message')
def handle_send_message_event(data):
    myapp_obj.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('join_room')
def handle_join_room_event(data):
    myapp_obj.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    myapp_obj.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if roomz.find_one({'code' : code}) == None:
            break
    return code

