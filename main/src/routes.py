#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import render_template, request

from run import emails, todos, users

#render index route
@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/index.html", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#add emails to database
@myapp_obj.route('/sendMail', methods=['GET', 'POST'])
def sendEmail():
    if request.method == 'POST':
        emails.insert_one({'sender': 'test sender', 'subject': 'test subject', 'message': 'test message'})
        return render_template('mailroom.html', message='message sent')
    else:
        return render_template('mailroom.html', message='message not sent')

#list emails from database
@myapp_obj.route('/mailroom', methods=['GET', 'POST'])
def listEmails():
    maillist = emails.find()
    return render_template('mailroom.html', emails=maillist)

#render todolist
@myapp_obj.route('/todolist', methods=['GET', 'POST'])
def todo():
    return render_template('todo.html')

#add item to todo list database
@myapp_obj.route('/addtodo', methods=['GET', 'POST'])
def addTodo():
    if request.method == 'POST':
        todoitem = request.form['todoitem']
        todos.insert_one({'item': todoitem})
        getTodoItem = todos.find()
        return render_template('todo.html', todos=getTodoItem)
    return render_template('todo.html', todos='Todo Not Rendered')

#remove item from todo list database collection
@myapp_obj.route('/removetodo', methods=['GET', 'POST'])
def remTodo():
    if request.method == 'POST':
        todos.delete_one({})
        getTodoItem = todos.find()
        return render_template('todo.html', todos=getTodoItem)
    return render_template('todo.html', todos='Todo Not Rendered')

@myapp_obj.route('/logout')
def logout():
    return render_template('logout.html')

@myapp_obj.route('/login')
def login():
    return render_template('log_in.html')

@myapp_obj.route('/register')
def register():
    return render_template('register.html')