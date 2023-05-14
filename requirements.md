## Functional Requirements

1. User Registration(Anthony, Hana)
2. User Login(Minh)
3. Undo messaging and unsend emails(Mj(Marlon))
4. Compose realtime message to chat with another user(Hana)
5. Todo List (Using external API)(Mj)
6. Users can change their password upon providing the correct informations(Hana)
7. Compose message to send email to another user(Mj)
8. User creates block list to stop someone sending email or chat to them(Mj)
9. User Logout(Hana, Minh)
10. Notification for new messages, emails(Mj, Minh)
11. Users are able to attach images to emails(Mj)
12. Users send message request to a designated recipient(Hana, Anthony)
13. Delete account(Hana)

## Non-functional Requirements

1. UI interactive interface (or using elements from bootstrap)(Minh, Anthony)
2. Light Mode and Dark Mode(Minh)

## Use Cases

1. User Registration

- **Pre-condition:**

  1. User has a working email
  2. User has a valid username

- **Trigger:** User selects “Register Account” button

- **Primary Sequence:**

  1. User enters full name
  2. User enters valid email address
  3. User enters password
  4. User clicks “Register” button
  5. User gets redirected to email inbox

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
  4. User click "confirm" button
  5. System verifies the account and updates new password for that user

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

  1. System displays error "Cannot find user"

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

6. User creates block list to stop someone sending email or chat to them

- **Pre-condition:**

  1. User is already registered with the email client
  2. User has logged in

- **Trigger:** User clicks “Block user" button

- **Primary Sequence:**

  1. System displays all existing users
  2. Select a user to block
  3. Click on the 'block user' button to block the selected user
  4. Blocked user is added to the list

- **Primary Postconditions:** The blocked user can not chat or send email to the one who blocks them

- **Alternate Sequence:** The blocked user already exists

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

  1. User goes to the the account page to start the process
  2. Clicks onto the 'logout' botton and confirms to log out on an alert
  3. The system redirects to after logout page notifying the logout was successful

- **Primary Postconditions:** User is successfully logged out from their account and is redirected to log in page

8. Notification for new messages, emails

- **Pre-condition:** Sender has logged in and directed to email inbox 

- **Trigger:** Email sent button or chat sent button

- **Primary Sequence:**

  1. The system displays a notification bar on top of the screen of the receiver
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
