from flask_wtf import FlaskForm
from flask_wtf.recaptcha import widgets
from wtforms import TextField, FileField
from wtforms.fields.simple import HiddenField
from wtforms.validators import Required
from wtforms.widgets import TextArea


class NotificationForFindingMusicianForm(FlaskForm):
    title = TextField('Title', [Required(message='Please, provide the title for your notification')])
    description = TextField('Description',[Required(message='Provide a description')], widget=TextArea())
    preferable_genres = TextField('Genres', [Required(message='Tell what are the musical genres ')])
    location = TextField('Location', [Required(message='Provide a location')])
    instruments = TextField('Musical instruments ', [Required(message='Tell what instruments do want to add to your band')])
    band_id = HiddenField()


class NotificationForFindingBandForm(FlaskForm):
    title = TextField('Title', [Required(message='Please, provide the title for your notification')])
    description = TextField('Description',[Required(message='Provide a description')], widget=TextArea())
    preferable_genres = TextField('Genres', [Required(message='Tell what are the musical genres ')])
    location = TextField('Location', [Required(message='Provide a location')])
    instruments = TextField('Musical instruments', [Required(message='Tell what instruments do want to add to your band')])
    musician_id = HiddenField()