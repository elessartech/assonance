from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app.config.from_object('config')

login_manager = LoginManager(app)

db = SQLAlchemy(app)

from application import controllers
from application.auth import controllers
from application.notifications import controllers
from application.auth.models import User
from application.util.security import encrypt_password

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.create_all()

admin = User.query.filter_by(email="admin@test.com").first()
if not admin:
    new_admin_user = User("admin", "admin@test.com", "admin", encrypt_password("admin"))
    db.session().add(new_admin_user)
    db.session().commit()