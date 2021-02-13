from application import db


class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

    def get_id(self):
        return self.id  


class User(Base):
    __tablename__ = 'users'

    name = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    role = db.Column(db.String(128),  nullable=False)
    password = db.Column(db.String(192),  nullable=False)

    def __init__(self, name, email, role, password):
        self.name = name
        self.email = email
        self.role = role
        self.password = password
    
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
       return True

    def has_roles(self, *args):
        return set(args).issubset({role for role in self.roles()})

    def roles(self):
        if self.role == "musician":
            return ["musician"]
        elif self.role == "band":
            return ["band"]
        else:
            return ["admin"]


class Media(Base):
    __tablename__ = 'medias'

    facebook = db.Column(db.String(128),  default=False, unique=True)
    spotify = db.Column(db.String(128),  default=False, unique=True)
    souncloud = db.Column(db.String(128),  default=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, facebook, spotify, souncloud, user_id):
        self.name = facebook
        self.proficiency = spotify
        self.souncloud = souncloud
        self.user_id = user_id
    
    