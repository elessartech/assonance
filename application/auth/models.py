from application import db

class User(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    
class Musician(User):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firstname = db.Column(db.String(128),  nullable=False)
    lastname = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    instruments = db.Column(db.String(192), nullable=False)
    facebook = db.Column(db.String(192), default=None)
    spotify = db.Column(db.String(192), default=None)
    soundcloud = db.Column(db.String(192), default=None)
    avatar = db.Column(db.LargeBinary, default=None) 

    def __init__(self, firstname, lastname, email, password, instruments, facebook, spotify, soundcloud):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.instruments = instruments
        self.facebook = facebook
        self.spotify = spotify
        self.soundcloud = soundcloud

    def get_id(self):
        return self.id  
    
    def get_avatar(self):
        return self.avatar

    def set_avatar(self, avatar):
        self.avatar = avatar

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
       return True

    def roles(self):
        return ["MUSICIAN"]
        
    def has_roles(self, *args):
        return set(args).issubset({role for role in self.roles()})

class Band(User):
    __tablename__ = 'bands'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    current_member_num = db.Column(db.Integer(), nullable=False)
    genres = db.Column(db.String(192), nullable=False)
    facebook = db.Column(db.String(192), default=None)
    spotify = db.Column(db.String(192), default=None)
    soundcloud = db.Column(db.String(192), default=None)
    avatar = db.Column(db.LargeBinary, default=None)

    def __init__(self, title, email, password, current_member_num, genres, facebook, spotify, soundcloud):
        self.title = title
        self.email = email
        self.password = password
        self.current_member_num = current_member_num
        self.genres = genres
        self.facebook = facebook
        self.spotify = spotify
        self.soundcloud = soundcloud

    def get_id(self):
        return self.id  

    def set_avatar(self, avatar):
        self.avatar = avatar

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
       return True

    def roles(self):
        return ["BAND"]

    def has_roles(self, *args):
        return set(args).issubset({role for role in self.roles()})