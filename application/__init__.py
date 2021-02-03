from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app.config.from_object('config')
app.secret_key = getenv("SECRET_KEY")

login_manager = LoginManager(app)
login_manager.blueprint_login_views = {  
    'musician':  "auth.musician_login",  
    'band': "auth.band_login",  
} 
#login_manager.login_view = 'login'

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from application.auth import controllers
from application.auth.models import Band, Musician
from application.musician import controllers

@login_manager.user_loader
def load_user(user_id):
    if session.get('band'):
        return Band.query.get(int(user_id))
    elif session.get('musician'):
        return Musician.query.get(int(user_id))
    else:
        return None


db.create_all()