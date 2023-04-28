from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
	firstname = StringField('First Name', validators = [DataRequired()])
	lastname = StringField('Last Name', validators = [DataRequired()])
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField('Register')
#validates if username is unique. if unique return true if not return false
	def validate_username(self, username):
		if User.query.filter_by(username=username.data).first() is None:
			return True
		return False
