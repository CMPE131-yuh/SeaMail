#import call for myapp_obj
from src import myapp_obj

#import flask libraries
from flask import send_file, send_file, render_template, request, redirect, url_for, session, flash
from flask_socketio import send
from bson.objectid import ObjectId
from bson import Binary
from PIL import Image
from matplotlib.pyplot import imshow, show
import codecs
import base64

#import basic python libraries for usage
import io
import random
from string import ascii_uppercase

#import db collection objects from run.py
from run import emails, todos, users, chat_history, grid_fs, blocked, blockedEmails, image, requests, mongo

#make app object secret key
myapp_obj.secret_key = "SEAMAIL.HQ"


#render index route
@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/index.html", methods=['GET', 'POST'])
def index():
    return render_template('index.html') #render starting index page

#add emails to database
@myapp_obj.route('/sendMail', methods=['GET', 'POST'])
def sendEmail():
    if request.method == 'POST':
        sub = request.form['sub'] #grab subject line for email from frontend
        msg = request.form['msg'] #grab message from text area to use for email from frontend
        rec = request.form['recipe'] #recipient information grabbed from frontend form
        if blocked.count_documents({'username': rec, 'userBlock': session['user']}) != 0: #if the sender is blocked from the recipient run if block
            blockedEmails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'notify': True}) #email from blocked user gets sent to blockedEmails database
            flash("This User Has Blocked You") #alert current user that the recipient blocked them
            return redirect(url_for('listEmails'))
        else: #if user not blocked, run code block
            emails.insert_one({'username': rec, 'sender': session['user'], 'subject': sub, 'message': msg, 'delete': False, 'hasImg': False, 'notify': True}) #insert new email into collection for recipient's mailroom
            return redirect(url_for('listEmails')) #render mailroom
    else:
        return render_template('mailroom.html', message='message not sent', current_user = session['user']) #error handling in case message doesn't go through, will render webpage with error message

#list emails from database
@myapp_obj.route('/mailroom', methods=['GET', 'POST'])
def listEmails():
    if request.method == 'GET':
        maillist = emails.find({'username': session['user']}) #find emails in database that are specific to the current session user
        if(emails.count_documents({'username': session['user'], 'notify': True}) != 0): #if user has emails, notify in webpage
            flash("You Got Mail!") #alert message to notify user for emails
            return render_template('mailroom.html', emails=maillist, current_user = session['user']) #render list of emails
        return render_template('mailroom.html', emails=maillist, current_user = session['user']) #render list of emails
    else:
        return render_template('mailroom.html', message='No Emails At This Time', current_user = session['user']) #error handling in case no emails or something wrong with listing emails

#list outbox emails from database
@myapp_obj.route('/outbox', methods=['GET', 'POST'])
def listOutbox():
    maillist = emails.find({'delete': False}) #grab sent mail from the database for unsending
    return render_template('outbox.html', sent=maillist, current_user = session['user']) #render outbox page with mail grabbed from emails collection

#unsend emails for both sender and receiver
@myapp_obj.route('/unsendEmail/<oid>', methods=['GET', 'POST'])
def unsendEmail(oid):
    if request.method == 'POST':
        emails.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}}) #update email ready for delete by setting delete value to True, grabs email from ObjectID
        emails.delete_one({'delete': True}) #delete emails that have delete value set to True
        return redirect(url_for('listOutbox')) #render listoutbox to render outbox page again after email gets unsent
    return render_template('outbox.html', sent='Error Loading Outbox') #error handling to render error message

#delete email for the current user's mailroom
@myapp_obj.route('/delEmail/<oid>', methods=['GET', 'POST'])
def delEmail(oid):
    if request.method == 'POST':
        emails.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}}) #after grabbing objectid, update delete item to True to mark item for delete
        emails.delete_one({'delete': True}) #delete the newly set True value
        return redirect(url_for('listEmails')) #redirect to mailroom to list newly updated list of emails
    return render_template('mailroom.html', emails='Error Loading Mailroom') #error handling, render error message if error

#render todolist
@myapp_obj.route('/todolist', methods=['GET', 'POST'])
def todo():
    todolist = todos.find({'username': session['user']}) #grab todos from todos collection based on current session user
    return render_template('todo.html', todos=todolist, username=session['user']) #render todolist page with specific todos grabbed from previous line

#add item to todo list database
@myapp_obj.route('/addtodo', methods=['GET', 'POST'])
def addTodo():
    if request.method == 'POST':
        todoitem = request.form['todoitem'] #get form submission into todoitem
        todos.insert_one({'username': session['user'], 'item': todoitem, 'delete': False}) #insert new todoitem grabbed from form submission
        getTodoItem = todos.find({'username': session['user']}) #grab todoitems again from todos collection
        return redirect(url_for('todo')) #redirect to todo to render todolist page
    return render_template('todo.html', todos='Todo Not Rendered') #error handling in case above code block not rendered

#remove item from todo list database collection
@myapp_obj.route('/removetodo/<oid>', methods=['GET', 'POST'])
def remTodo(oid):
    if request.method == 'POST':
        todos.update_one({'_id': ObjectId(oid)}, {'$set': {'delete': True}}) #update item based on grabbed object id to be marked for deletion
        todos.delete_one({'delete': True}) #delete item that has been marked for deletion
        return redirect(url_for('todo')) #redirect to todolist to be rendered
    return render_template('todo.html', todos='Todo Not Rendered') #error handling, renders error message

#logout funcionality, logs out current user session
@myapp_obj.route('/logout', methods = ['GET', 'POST'])
def logout():
    todolist = todos.find({'username' : session['user']}).count()
    mails = emails.find({'username' : session['user']}).count()
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
    return render_template('logout.html', current_user = session['user'], todos = todolist, mails = mails)

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

#Change password upon providing correct information
@myapp_obj.route('/change_password', methods = ['GET', 'POST'])
def changePassword():
    if request.method == 'POST':
        name = request.form['username']
        new = request.form['new_password']
        curr = request.form['current_password']
        if 'back' in request.form:
            return redirect(url_for('logout'))
        check = users.find_one({'$or': [{'username' : name, 'password':curr},{'email' : name, 'password' : curr}]})
        
        #Notifying if the user entered wrong username, email, or password
        if check == None:
            return """
            <div align='center'>
                <h3>Wrong combination of username/email and password</h3>
                <h3>Please try again!</h3>
                </br>
                <a href = "change_password">Return to the previous page</a>
            </div>
            """
        #Notifying when 2 inputs to check password do not match
        elif request.form['current_password'] != request.form['check_current']:
            return """
            <h3>The passwords don't match!</h3>
            </br>
            <a href = "change_password">Return to the previous page</a>
            """
        #User is granted the permission to change password 
        else:
            if users.find_one({'username' : name}):
                query = {'username' : request.form['username']}
                update = { "$set": { "password": new } }
                users.update_one(query, update)
            else:
                query = {'email' : request.form['username']}
                update = { "$set": { "password": new } }
                users.update_one(query, update)
            return redirect(url_for('logout'))

    return render_template('password_change.html')

#Entrance page before entering a chatroom with selected user
@myapp_obj.route('/enterance', methods = ['GET', 'POST'])
def enterance():
    if request.method == 'POST':
        recipient = request.form['recipient']
        num = requests.find({'$or' : [{'request' : session['user'] , 'receive' : recipient}, {'receive' : session['user'], 'request' : recipient}]}).count()
        #User cannot choose non existent user and self as a recipient
        if users.find_one({'username' : recipient}) == None or recipient == session['user']:
            flash('Invalid username!')
        #Create a new request if both users have not yet requested to start a chat
        elif num == 0:
            requests.insert_one({'request': session['user'], 'receive' : recipient, 'request2' : 'True', 'receive2' : 'False'})
            flash('Request successfully sent to ' + recipient + ' !')
        #Notify user if chat request to the selected user is already made 
        elif requests.find_one({'request' : session['user'], 'receive2' : 'False'}) != None:
            flash('You have already requested the user to start a chat!\n Please wait for the other user to accept your request.')
        #Notify user if the selected user has made chat request and waiting for the user to accept
        elif requests.find_one({'receive' : recipient, 'receive2' : 'False'}) != None:
            flash('This user has already sent you a request. \nPlease go to account page >> request list, to accept the request.')
        #Start the chat if both users accepted the request
        else:
            list = chat_history.find({'$or': [{'recipient' : recipient, 'sender':session['user']},{'recipient' : session['user'], 'sender' : recipient}]})
            session['recipient'] = recipient
            return redirect(url_for('room'))
    req = requests.find({'receive' : session['user'], 'receive2' : 'False'})
    accepted = requests.find({'$or' : [{'request' : session['user'], 'receive2' : 'True'}, {'receive' : session['user'], 'receive2' : 'True'}]})
    return render_template('enterance.html', user = session['user'], requests = req, accepted = accepted)

#route for chatroom
@myapp_obj.route('/room', methods = ['GET', 'POST'])
def room():
    list = chat_history.find({'$or': [{'recipient' : session['recipient'], 'sender':session['user']},{'recipient' : session['user'], 'sender' : session['recipient']}]})
    if request.method == 'GET':
        return render_template('room.html', chats = list)
    #User exiting from a chatroom
    if request.method == 'POST':
        if 'exit' in request.form:
            session.pop('recipient')
            return redirect(url_for('enterance'))

        new_msg = request.form['message']
        chat_history.insert_one({'sender' : session['user'], 'recipient' : session['recipient'], 'message' : new_msg})
        list = chat_history.find({'$or': [{'recipient' : session['recipient'], 'sender':session['user']},{'recipient' : session['user'], 'sender' : session['recipient']}]})
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
        userBlocked = users.find_one({'_id': ObjectId(oid)}) #find user by object id
        if userBlocked:
            nameBlocked = userBlocked['username'] #get the username of that user after finding object id
            blocked.insert_one({'username': session['user'], 'userBlock': nameBlocked}) #insert blocked username into blocked collection
            flash("User Blocked") #notify user that the person they blocked has been blocked
            return redirect(url_for('listAccounts')) #redirect to list of accounts
    
#remove user from current user's blocked user emails
@myapp_obj.route('/unblock/<oid>', methods = ['GET', 'POST'])
def unblock(oid):
    if request.method == 'POST':
        userBlocked = users.find_one({'_id': ObjectId(oid)}) #find user by object id
        if userBlocked:
            nameUnblocked = userBlocked['username'] #get the username of that user after finding object id
            blocked.delete_one({'_id': ObjectId(oid)})
            if blockedEmails.count_documents({'sender': nameUnblocked}) != 0: #check to seee if the user being unblocked has emails that were sent to blockedEmails collection
                blockedEmail = blockedEmails.find_one({'sender': nameUnblocked}) #find blockedEmails based on the username that was blocked
                emails.insert_one(blockedEmail) #insert those blocked emails into the emails collection so it can be listed in the mailroom
        blocked.delete_one({'username': session['user'], 'userBlock': nameUnblocked}) #delete blocked username from the blocked collection
        flash("User Unblocked") #notify current user that the user they unblocked has been unblocked
        return redirect(url_for('listAccounts')) #redirect to list accounts page
    
#Remove a user from the request list when declined, and open a message thread when accepted
@myapp_obj.route('/request/<oid>', methods = ['GET', 'POST'])
#The object id provides the unique id tied to each entry of the request database in mongodb
def acceptOrDecline(oid):
    recipient = requests.find_one({'_id' : ObjectId(oid)}).get('request')
    if request.method == 'POST':
        if 'accept' in request.form:
            query = {'_id' : ObjectId(oid)}
            update = { "$set": { "receive2": 'True' } }
            #update request status to accepted
            requests.update_one(query, update)
            flash('Accepted chat request from ' + recipient)
        elif 'decline' in request.form:
            #update request status by deleting the request list
            requests.delete_one({'_id' : ObjectId(oid)})
            flash('Declined chat request from ' + recipient)
        return redirect(url_for('enterance'))

#Enter the chat with selected user
@myapp_obj.route('/enter/<oid>', methods = ['GET', 'POST'])
def enterChat(oid):
    if request.method == 'POST':
        if requests.find_one({'_id' : ObjectId(oid)}).get('request') != session['user']:
            session['recipient'] = requests.find_one({'_id' : ObjectId(oid)}).get('request')
        else:
            session['recipient'] = requests.find_one({'_id' : ObjectId(oid)}).get('receive')
        
    return redirect(url_for('room'))
