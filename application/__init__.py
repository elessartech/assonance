from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import os

csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app.config.from_object('config')

login_manager = LoginManager(app)

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from application.auth import controllers
from application.notifications import controllers
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


db.create_all()