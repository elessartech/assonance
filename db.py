from app import app
from flask_sqlalchemy import SQLAlchemy

app.config.from_object('config')

db = SQLAlchemy(app)