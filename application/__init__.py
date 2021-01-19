from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app.config.from_object('config')
app.secret_key = getenv("SECRET_KEY")

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from application.auth.controllers import auth as authentication_module
app.register_blueprint(authentication_module)
db.create_all()