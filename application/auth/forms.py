from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.fields.core import RadioField
from wtforms.validators import Required, Email

class LoginForm(FlaskForm):
    email = TextField('Email Address', [Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])

class SignupForm(FlaskForm):
    role = RadioField('Role', choices=['musician', 'band'], default='musician', validators=[Required()])
    name = TextField('First name', [Required(message='Please, provide your title')])
    email = TextField('Email Address',[Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])
    confirm_password = PasswordField('Confirm Password', [Required(message='Confirm your password please')])