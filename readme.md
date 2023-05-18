# Project Name
- Marlon Burog (4-gent) (Team Lead)
- Anthony Luu (EdotAnt)
- Minh Phong Do (stanphong)
- Hana Suzuki (Hana1107)

# Implementation
* git clone repository first to have the web application
* change directories into the main directory that includes a Requirements.txt document
* from there, run python3 -m pip3 install -r Requirements.txt to download required packages
* then in the main, run python3 run.py to start the development environment on localhost:5000
* then you are now able to use the web application

# Functional Requirements
1. User Registration(Hana, Anthony)
2. User Login(Minh)
3. Undo messaging and unsend emails(Marlon)
4. Compose realtime message to chat with another user(Hana)
5. Todo List (Using external API)(Marlon)
6. Users can change their password upon providing the correct informations(Hana)
7. Compose message to send email to another user(Marlon)
8. User creates block list to stop someone sending email or chat to them(Marlon)
9. User Logout(Hana)
10. Notification for new messages, emails(Minh, Marlon)
11. Users send message request to a designated recipient(Hana)
12. Delete account(Hana, Anthony)

## Non-functional Requirements
1. UI interactive interface (or using elements from bootstrap)(Minh, Anthony)
2. Light Mode and Dark Mode(Minh)

# Basic Functions
Below are the basic functions that are offered on SeaMail and instructions on how to access them
1. Register Account
	- From the main page click on the register button, then fill out username, password, and email, then finish register
2. Login
	- From the main page click on the login button, fill in your username and password, then click the login button
3. Send Mail
	- After succesfully logging in or by clicking the Seamail button on the taskbar, you will be sent to the mailroom page, where you can email another registered user by filling out the username, subject, and message boxes, then clicking the send email button.
4. View Mail
	- From the mailroom page, you can view emails that have been sent to you under the send mail boxes.
5. Chat
	- Click on the Chat link on the navigation bar, it will redirect you the Chat Main Page
	- You can send the message to a recipient by typing their username and click "start a new message thread"
	- Once you send a message to a new person, it will appear on the request list on the right side of the recipient. You can click accept or decline to move it to the message thread
	- You can start the chat from the message threads on the left side by click enter the chat. It will redirect you to the chat room with that username, from there you can send message or exit the chat.
6. Todo List
	- The todo list can be accessed by clicking the Todo List button on the taskbar. From the todo list page, you can add a todo even to your list by filling out the Todo item: box, then clicking the add Todo button. These todos can also be removed by clicking the remove todo button for your todo event.
7. Block 
	- To block a user from sending you messages, you can a access a list of other registered users in the other users button on the task bar, from there you will be able to view a list of all other registered users where you can block/unblock by clicking the block or unblock button next to each user's name.
8. Log Out
	- Click on the your account button on the taskbar, then click the log out button
9. Delete Account
	- Click on the your account button on the taskbar, then click the delete account button
10. Night Mode 
	- A night mode function can be toggled on and off by clicking the dark mode switch on the top right corner of the taskbar. 
11. Change password
	- Go to Your account on the navigation bar, click on change password. It will redirect you to the change password page
	- Type in your username, password, new password, then click change. It will redirect you back to the account page, and your password has sucessfully changed.

# Test Account
- A test account is avaivable to use to view the basic functions of the website

| Username  	| Password 	|
| ------------- | ------------- |
| ming  	| 12345678  	|
| test  	| test  	|

