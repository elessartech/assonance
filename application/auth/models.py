from application import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firstname = db.Column(db.String(128),  nullable=False)
    lastname = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    instruments = db.Column(db.String(192), nullable=False) # either "band" or "musician" or "admin"

    def __init__(self, firstname, lastname, email, password, instruments):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.instruments = instruments

    def get_user_id(self):
        return self.id  