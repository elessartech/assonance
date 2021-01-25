from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app.config.from_object('config')
app.secret_key = getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from application.auth import controllers
from application.auth.models import User
from application.musician import controllers

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db.create_all()