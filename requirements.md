## Functional Requirements

1. User Registration
2. User Login
3. Undo messaging and unsend emails
4. Compose realtime message to chat with another user
5. Todo List (Using external API)
6. Users can change their password upon providing the correct informations
7. Compose message to send email to another user
8. User creates block list to stop someone sending email or chat to them
9. User Logout
10. Notification for new messages, emails
11. Users are able to attach images to emails
12. Users send message request to a designated recipient
13. Delete account

## Non-functional Requirements

1. UI interactive interface (or using elements from bootstrap)
2. Light Mode and Dark Mode

## Use Cases

1. User Registration

- **Pre-condition:**

  1. User has a working email
  2. User knows his/her/their birth information

- **Trigger:** User selects “Register Account” button

- **Primary Sequence:**

  1. User enters full name
  2. User enters birthday
  3. User enters valid email address
  4. User enters password
  5. User clicks “Register” button

- **Primary Postconditions:** User can log in with the registered account

- **Alternate Sequence:** User does not fill in email address/ enters invalid email address when user clicks “Register” button

  1. System displays error message(Information is not filled out/valid)
  2. System stays on register page

- **Alternate Sequence:** User does not fill in password when user clicks “Register” button

  1. System displays error message(Password is not filled out)
  2. System stays on register page

2. User Login

- **Pre-condition:** User has a register account with username and corresponding password.

- **Trigger:** User presses login button

- **Primary Sequence:**

  1. User enters registered email address
  2. User enters password
  3. User clicks “Log-in” button
  4. System redirects user to home page

- **Primary Postconditions:** User has successfully logged into email client and is redirected to the home page

- **Alternate Sequence:** User enters incorrect password.

  1. System displays error message
  2. System stays on the login page

3. Users can change their password and username upon providing the correct informations

- **Pre-condition:**

  1. User has to be a registered user
  2. User needs to be logged in
  3. User navigate to the account page

- **Trigger:** Change password button

- **Primary Sequence:**

  1. System redirects user to a new page, and open a form for user reset password
  2. User enters their username, current password, and new password
  3. User retype new password in another form
  4. User click "confirm" button
  5. System verifies the account, updates new password for that user, and notifies user "new password updated"

- **Primary Postconditions:**

  1. Users have successfully changed their password

- **Alternate Sequence:** Wrong username or password

  1. System displays error message "Wrong username or password"
  2. Returns to the password change page to reenter their credentials for another attempt

4. Compose real-time message to chat with another user

- **Pre-condition:**

  1. Both users have registered accounts
  2. Both users are logged in

- **Trigger:** Chat button

- **Primary Sequence:**

  1. System redirects user to chat window
  2. Sender inputs recipient username/email to chat with
  3. Sender drafts message in text area
  4. Sender clicks on the send button
  5. Sent messages appear in chat window that can be seen by both sender and receiver

- **Primary Postconditions:**

  1. Messaging successfully happens
  2. Sender sent message
  3. Receiver receives message

- **Alternate Sequence:** Input wrong recipient

  1. System displays error "Can not find username"

5. Compose message to send email to another user

- **Pre-condition:**

  1. Both users have registered accounts
  2. Sender selects a recipient

- **Trigger:** Compose email button

- **Primary Sequence:**

  1. Sender inputs recipient address/username/email
  2. Sender drafts message in text areas
  3. Sender click "send" button
  4. Sender receives a sent receipt

- **Primary Postconditions:**

  1. Messaging successfully happens
  2. Sender sent email
  3. Receiver receives email

- **Alternate Sequence:** Input wrong recipient

  1. User is shown to not exist
  2. Message is sent to wrong recipient

- **Alternate Sequence:** File attachment

  1. Attach PDF, docs, etc files
  2. Attach jpeg, png, etc files

6. User creates block list to stop someone sending email or chat to them

- **Pre-condition:**

  1. User is already registered with the email client
  2. User has logged in

- **Trigger:** User clicks “Block list” button

- **Primary Sequence:**

  1. System displays a window with a list of blocked users and a form to add new user to the list
  2. User fills the username to be blocked in the form
  3. User clicks “confirm” button
  4. Blocked user is added to the list

- **Primary Postconditions:** The blocked user can not chat or send email to the one who blocks them

- **Alternate Sequence:** The blocked user is already existed

  1. System displays error message("Already blocked")
  2. No new user is added to block list

- **Alternate Sequence:** The blocked user can not be detected
  1. System displays error message("Can not find username") 

7. User Logout

- **Pre-condition:**

  1. The user is logged in
  2. The user wishes to no longer be logged in

- **Trigger:** Clicking on ‘logout’ button

- **Primary Sequence:**

  1. Systems displays a warning message to log out with 'ok' button and 'stay logged in' button
  2. User confirms logging out by clicking ‘ok’ on a warning
  3. The system redirects to login page

- **Primary Postconditions:** User is successfully logged out from their account and is redirected to log in page

- **Alternate Sequence:** Clicking ‘stay logged in’ button on the warning

  1. User remains logged in and goes back to the user account page

8. Notification for new messages, emails

- **Pre-condition:** Sender has logged in with composed chat or email message

- **Trigger:** Email sent button or chat sent button

- **Primary Sequence:**

  1. The system displays a notification bar on top of the screen of the receiver with the name of sender
  2. Receiver presses on the notification bar 
  3. System redirects user to the chat window or mail window depending on the type of new message

- **Primary Postconditions:**

  1. The notification can not arrived before the actual message was sent
  2. A notification bar appears on the window of the correct receiver when there are new messages

- **Alternate Sequence:** Stack notifications when the receiver has not seen new messages

  1. The notification bar displays number of new mail or chat
  2. User presses on the notification window to see list of new mails or messages

- **Alternate Sequence:** User press on the close button to ignore new notifications

  1. The notification window disappears
