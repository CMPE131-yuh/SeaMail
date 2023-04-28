from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from .forms import ComposeForm
from .forms import LoginForm
from .forms import RegisterForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_require
from  werkzeug.security import generate_password_hash
# Route for Register page
@app.route('/register', methods =['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
	#check for unique username
	if form.validate_username(form.username)== True:
		#if true, creates new user object conataining name, username, hashed password, and adds it to database
		user = User(name=form.firstname.data + " " + form.lastname.data, username=form.username.data, password=generate_password_hash(form.password.data))
		#adds user to db
		db.session.add(user)
		db.session.commit()
		#redirect to login
		return redirect(url_for('login'))
    return render_template('register.html', form = form)
