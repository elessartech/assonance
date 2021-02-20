from flask_wtf import FlaskForm
from wtforms import TextField, SelectField
from wtforms.fields.simple import HiddenField
from wtforms.validators import Required
from wtforms.widgets import TextArea
from wtforms.fields.core import RadioField
from application.util.data import get_genres, get_countries, get_instruments

class NewNotification(FlaskForm):
    title = TextField('Title', [Required(message='Please, provide the title for your notification')])
    description = TextField('Description',[Required(message='Provide a description')], widget=TextArea())
    publisher_id = HiddenField()
    genre = SelectField('Genres', [Required(message='Select genres')], choices=get_genres())
    country = SelectField('Country', [Required(message='Select a country')], choices=get_countries())
    instrument = SelectField('Instruments', [Required(message='Select instruments')], choices=get_instruments())

class FilterNotifications(FlaskForm):
    show = RadioField('Show notifications', choices=['all notifications', 'my notifications'], default='all notifications', validators=[Required()])
    filter = RadioField('Filter by:', choices=['no filter', 'instruments', 'genres', 'locations'], default='no filter', validators=[Required()])