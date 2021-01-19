from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(FlaskForm):
    email = TextField('Email Address', [Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])

class SigninForm(FlaskForm):
    firstname = TextField('First name', [Required(message='Please, provide your first name')])
    lastname = TextField('Last name', [Required(message='Please, provide your last name')])
    email = TextField('Email Address',[Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])
    confirm_password = PasswordField('Confirm Password', [Required(message='Confirm your password please')])
    instruments = TextField('Musical Instruments', [Required(message='Provide musical instruments that you play')])