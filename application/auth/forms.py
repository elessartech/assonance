from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(FlaskForm):
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')])