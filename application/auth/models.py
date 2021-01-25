from application import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

# Make 2 classes for 2 types of users: bands and musicians
class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firstname = db.Column(db.String(128),  nullable=False)
    lastname = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    instruments = db.Column(db.String(192), nullable=False)

    def __init__(self, firstname, lastname, email, password, instruments):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.instruments = instruments

    def get_id(self):
        return self.id  

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
       return True
    
    def roles(self):
        return ["MUSICIAN", "BAND", "ADMIN"]