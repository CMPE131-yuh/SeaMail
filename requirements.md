## Functional Requirements

1. User Registration
2. User Login
3. Develop a login database for user login handling with standard CRUD operations
4. Chat/Messaging functionality
5. Todo List (Using external API)
6. Create a mailing database to hold emails that will be posted to user mailroom after login
7. Mailer/Mail Generation
8. Customization of Website
9. User Logout
10. Notification functionality
11. Users able to attach images to their email as well as send them in chat
12. Users send message request to a designated recipient

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
  6. The informations are sent and stored in a database of accounts

- **Primary Postconditions:** The information is stored, secured and retrievable when they are requested

- **Alternate Sequence:** User does not fill in email address/ enters invalid email address when user clicks “Register” button

  1. System displays error message(Information is not filled out/valid)
  2. System stays on register page

- **Alternate Sequence:** User does not fill in password when user clicks “Register” button

  1. System displays error message(Password is not filled out)
  2. System stays on register page

2. User Login

- **Pre-condition:** User already has a email address and password registered with email client

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

3. Develop a login database for user login handling with standard CRUD operations

- **Pre-condition:**

  1. User has to be a registered user
  2. Must have a working username and password
  3. Python flask atlas external api to handle database collections

- **Trigger:**

  1. Text area for form input
  2. Login Button

- **Primary Sequence:**

  1. Client inputs credentials into username and password input fields
  2. Client hits login to send credentials through backend to fetch data through mongodb to make sure the credentials match
  3. Redirects to users mailroom

- **Primary Postconditions:**

  1. Credentials get sent to api call
  2. Redirects user to mailroom
  3. User’s emails are posted from collection in mongodb

- **Alternate Sequence:** Wrong user credentials

  1. Returns pop-up that credentials are incorrect
  2. User will have to re input correct credentials

4. Chat/Messaging functionality

- **Pre-condition:**

  1. Both users have registered accounts
  2. Both users are logged in
  3. User fills out messaging form

- **Trigger:** Send button

- **Primary Sequence:**

  1. Sender inputs recipient address/username/email
  2. Sender drafts message in text areas
  3. Sender performs trigger
  4. Message post request to messaging database
  5. From database, recipient performs get request, gets message from database

- **Primary Postconditions:**

  1. Messaging successfully happens
  2. Sender sends message
  3. Receiver receives message

- **Alternate Sequence:** Input wrong recipient

  1. User is shown to not exist
  2. Message is sent to wrong recipient

5. Mailer/Mail Generation

- **Pre-condition:**

  1. Both users have registered accounts
  2. Sender selects a recipient
  3. Users clicks on the email generation button

- **Trigger:** Send button

- **Primary Sequence:**

  1. Sender inputs recipient address/username/email
  2. Sender drafts message in text areas
  3. Sender performs trigger
  4. Message post request to messaging database
  5. From database, recipient performs get request, gets message from database

- **Primary Postconditions:**

  1. Messaging successfully happens
  2. Sender sends email
  3. Receiver receives email

- **Alternate Sequence:** Input wrong recipient

  1. User is shown to not exist
  2. Message is sent to wrong recipient

- **Alternate Sequence:** File attachment

  1. Attach PDF, docs, etc files
  2. Attach jpeg, png, etc files

6. Customization of Website

- **Pre-condition:**

  1. User is already registered with the email client
  2. User has logged in

- **Trigger:** User clicks “customize website” button

- **Primary Sequence:**

  1. User enters password
  2. User clicks 1 of 3 layout options
  3. User clicks “confirm” button

- **Primary Postconditions:** User is either redirected to the main page of the website with the selected layout or is still on the website customization page

- **Alternate Sequence:** User misspelled password when pressing “confirm” button

  1. System displays error message(incorrect password)
  2. System stays on website customization page

7. User Logout

- **Pre-condition:**

  1. The user is logged in
  2. The user wishes to no longer be logged in

- **Trigger:** Clicking on ‘logout’ or ‘sign out’ button

- **Primary Sequence:**

  1. User navigates to user account page
  2. Clicks on the log out button
  3. User confirms logging out by clicking ‘ok’ on a warning
  4. The system redirects to login page

- **Primary Postconditions:** User is successfully logged out from their account and is redirected to log in page

- **Alternate Sequence:** Clicking ‘stay logged in’ button on the warning

  1. User remains logged in and goes back to the user account page

8. Notification functionality

- **Pre-condition:** User logins and opens chat box or mail generator box

- **Trigger:** Email sent button or chat sent button

- **Primary Sequence:**

  1. User finishes composing messages in mail generator with receiver’s address or chat box
  2. User presses the sent button
  3. The mail system or chat box system will sent the notification according to the address of the receiver
  4. A small window on top of the screen of the receiver drop down with a message, either a new mail or a new message
  5. Receiver press on the window to directly go to the new mail or message

- **Primary Postconditions:**

  1. The notification can not arrived before the actual message was sent
  2. A notification window of the receiver screen drops down when someone sends new mail/ message.
  3. The notification windows must correspond to the new mail or message and appear in chronological order.

- **Alternate Sequence:** Stack notifications when the receiver is not logged in

  1. The notification window will have a message with the number of new mails/messages
  2. User pressing on the notification window will appear a list of new mails/messages

- **Alternate Sequence:** User press on the close button to ignore new notifications

  1. The notification window will disappear
