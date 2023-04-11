## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. User Registration
  A. Anthony
  B. Summary
    1. User enters account information to register his/her/their account in order to use the email client
  C. Precondition
    1. User has a working email
    2. User knows his/her/their birth information
  D. Trigger
    1. User selects “Register Account” button
  E. Primary Sequence
    1. User enters full name
    2. User enters birthday
    3. User enters valid email address
    4. User enters password
    5. User clicks “Register” button
  F. Alt. Sequence
    1. User does not fill in email address/ enters invalid email address when user clicks “Register” button
      a) System displays error message(Information is not filled out/valid)
      b) System stays on register page
    2. User does not fill in password when user clicks “Register” button
      a) System displays error message(Password is not filled out)
      b) System stays on register page
  G. Post Condition
    1. User information is now registered and user is redirected to home page or some information is invalid/missing and user stays on register page.
  H. Glossary
    1. User: person who has email and password registered in the email client
2. User Login
  A. Minh
  B. Use Case
    1. Summary
      a) Existing user logs in using their registered email address and password
    2. Precondition
      a) User already has a email address and password registered with email client
    3. Trigger
      a) Login button
    4. Primary Sequence
      a) User enters registered email address
      b) User enters password
      c) User clicks “Log-in” button
      d) System redirects user to home page
    5. Alt. Sequence
      a) User enters incorrect password
        (1) System displays error message
        (2) System stays on the login page
    6. Post condition
      a) User has successfully logged into email client and is redirected to the home page or has failed to login and is still on the login page
    7. Glossary
      a) User: person who has email and password registered in the email client

3. Develop a login database for user login handling with standard CRUD operations
    A. * Using mongodb atlas api
      1. Python flask atlas external api to handle database collections
    B. Use Case
      1. Summary
        a) MongoDB atlas database to store user credentials for future post requests
      2. Precondition
        a) User has to be a registered user
        b) Must have a working username and password
      3. Actors
        a) Client logging in
      4. Triggers
        a) Text area for form input
        b) Login Button
      5. Primary sequence
        a) Client inputs credentials into username and password input fields
        b) Client hits login to send credentials through backend to fetch data through mongodb to make sure the credentials match
        c) Redirects to users mailroom
      6. Alternate Sequence
        a) Wrong user credentials
          (1) Returns pop-up that credentials are incorrect
          (2) User will have to re input correct credentials
      7. Post Condition
        a) Credentials get sent to api call
        b) Redirects user to mailroom
        c) User’s emails are posted from collection in mongodb

4. Chat/Messaging functionality
  A. Mj/Hana
  B. Use Case
    1. Summary
      a) Messaging application that allows for direct messaging from one actor to another
    2. Precondition
      a) Both users have registered accounts
      b) Both users are logged in
      c) User fills out messaging form
    3. Actors
      a) Sender
      b) Recipient
    4. Triggers
      a) Send button
    5. Primary Sequence
      a) Sender inputs recipient address/username/email
      b) Sender drafts message in text areas
      c) Sender performs trigger
      d) Message post request to messaging database
      e) From database, recipient performs get request, gets message from database
    6. Alternate Sequence
      a) Input wrong recipient
        (1) User is shown to not exist
        (2) Message is sent to wrong recipient
    7. Post Condition
      a) Messaging successfully happens
      b) Sender sends message
      c) Receiver receives message

5. Todo List (External API?)
  A. Mj

6. Create a mailing database to hold emails that will be posted to user mailroom after login
  A. Hana
7. Mailer/Mail Generation
  A. Mj
  B. Use Case
    1. Summary
      a) The users will be able to generate an email to be sent to their desired recipient(s)
    2. Precondition
      a) Both users have registered accounts
      b) Sender selects a recipient
      c) Users clicks on the email generation button
    3. Actors
      a) Sender
      b) Recipient
    4. Triggers
      a) Send button
    5. Primary Sequence
      a) Sender inputs recipient address/username/email
      b) Sender drafts message in text areas
      c) Sender performs trigger
      d) Message post request to messaging database
      e) From database, recipient performs get request, gets message from database
    6. Alternate Sequence
      a) Input wrong recipient
        (1) User is shown to not exist
        (2) Message is sent to wrong recipient
      b) File attachment
        (1) Attach PDF, docs, etc files
        (2) Attach jpeg, png, etc files
    7. Post Condition
      a) Messaging successfully happens
      b) Sender sends email
      c) Receiver receives email

8. Customization of Website
  A. Anthony
  B. Use Case
  1. Summary
    a) Users are able to customize the format(positions of logout button, login button, register button, etc.) of the website to their liking.
  2. Pre-Condition
    a) User is already registered with the email client
    b) User has logged in
  3. Trigger: User clicks “customize website” button
  4. Primary Sequence:
    a) User enters password
    b) User clicks 1 of 3 layout options
    c) User clicks “confirm” button
    d)
  5. Alt. Sequence
    a) User misspelled password when pressing “confirm” button
      (1) System displays error message(incorrect password)
      (2) System stays on website customization page
  6. Post Condition
    a) User is either redirected to the main page of the website with the selected layout or is still on the website customization page
9. User Logout
  A. Hana
  B. Use Case
    1. Summary
      a) Users are able to log out from their account when the application is not in use
    2. Precondition
      a) The user is logged in
      b) The user wishes to no longer be logged in
    3. Actors
      a) Users
    4. Triggers
      a) Clicking on ‘logout’ or ‘sign out’ button
    5. Primary Sequence
      a) User navigates to user account page
      b) Clicks on the log out button
      c) User confirms logging out by clicking ‘ok’ on a warning
      d) The system redirects to login page
    6. Alternate Sequence
      a) Clicking ‘stay logged in’ button on the warning
        (1) User remains logged in and goes back to the user account page
    7. Post Condition
      a) User is successfully logged out from their account and is redirected to log in page

10. Notification functionality
  A. Minh
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

11. Users able to attach images to their email as well as send them in chat
  A. Hana
12. Users send message request to a designated recipient
  A. Mj/Hana


## Non-functional Requirements

1. UI interactive interface (or using elements from bootstrap)
2. Light Mode and Dark Mode

## Use Cases

1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...
2. Use Case Name (Should match functional requirement name)
   ...
