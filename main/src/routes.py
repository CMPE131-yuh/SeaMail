#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import render_template, request, redirect, url_for, session

from run import emails, todos, users

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
        emails.insert_one({'sender': 'test sender', 'subject': 'test subject', 'message': 'test message'})
        return render_template('mailroom.html', message='message sent', current_user = session['user'])
    else:
        return render_template('mailroom.html', message='message not sent', current_user = session['user'])

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

@myapp_obj.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        psw = request.form['password']
        if users.find_one({'username':name, 'password':psw}) != None:
            session['user'] = name
            return redirect(url_for('sendEmail'))
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
        new_user_email = request.form['email']
        new_user = {'username' : new_username, 'password' : new_user_password, 'email' : new_user_email}
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