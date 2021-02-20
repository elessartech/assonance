from flask_wtf import FlaskForm
from wtforms import TextField, SelectMultipleField, SelectField
from wtforms.fields.simple import HiddenField
from wtforms.validators import Required
from wtforms.widgets import TextArea
from wtforms.fields.core import RadioField
from application.util.data import get_genres, get_countries, get_instruments

class NewNotification(FlaskForm):
    title = TextField('Title', [Required(message='Please, provide the title for your notification')])
    description = TextField('Description',[Required(message='Provide a description')], widget=TextArea())
    publisher_id = HiddenField()
    genres = SelectMultipleField('Genres', [Required(message='Select genres')], choices=get_genres())
    country = SelectField('Country', [Required(message='Select a country')], choices=get_countries())
    instruments = SelectMultipleField('Instruments', [Required(message='Select instruments')], choices=get_instruments())

class FilterNotifications(FlaskForm):
    filter = RadioField('Filter by:', choices=['no filter', ' by publisher', 'by instruments', 'by genres', 'by location'], default='no filter', validators=[Required()])