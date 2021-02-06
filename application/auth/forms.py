from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.fields.core import RadioField
from wtforms.validators import Required, Email

class LoginForm(FlaskForm):
    role = RadioField('Role', choices=['musician', 'band', 'admin'], default='musician', validators=[Required()])
    email = TextField('Email Address', [Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])


class MusicianSignupForm(FlaskForm):
    firstname = TextField('First name', [Required(message='Please, provide your first name')])
    lastname = TextField('Last name', [Required(message='Please, provide your last name')])
    email = TextField('Email Address',[Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])
    confirm_password = PasswordField('Confirm Password', [Required(message='Confirm your password please')])
    instruments = TextField('Musical Instruments', [])
    facebook = TextField('Facebook', [])
    spotify = TextField('Spotify', [])
    soundcloud = TextField('SoundCloud', [])

class BandSignupForm(FlaskForm):
    title = TextField('First name', [Required(message='Please, provide your title')])
    email = TextField('Email Address',[Email(), Required(message='Incorrect email')])
    password = PasswordField('Password', [Required(message='Password must be provided.')])
    confirm_password = PasswordField('Confirm Password', [Required(message='Confirm your password please')])
    current_member_num = TextField('Current number of members', [Required(message='How many people are playing in your band?')])
    genres = TextField('Current number of members', [Required(message='What genres do you play in?')])
    facebook = TextField('Facebook', [])
    spotify = TextField('Spotify', [])
    soundcloud = TextField('SoundCloud', [])