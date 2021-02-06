from application import db

class Notification(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

class NotificationForFindingMusician(Notification):
    __tablename__ = 'notifications_for_finding_musicians'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(192), nullable=False)
    preferable_genres = db.Column(db.String(192), nullable=False)
    location = db.Column(db.String(192), nullable=False)
    instruments = db.Column(db.String(192), nullable=False)
    band_id = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.LargeBinary, default=None) 
    rendered_cover_image = db.Column(db.Text, default=None)
    likes = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, title, description, preferable_genres, location, instruments, band_id):
        self.title = title
        self.description = description
        self.preferable_genres = preferable_genres
        self.location = location
        self.instruments = instruments
        self.band_id = band_id

    def get_id(self):
        return self.id  

class NotificationForFindingBand(Notification):
    __tablename__ = 'notifications_for_finding_bands'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(192), nullable=False)
    instruments = db.Column(db.String(192), nullable=False)
    preferable_genres = db.Column(db.String(192), nullable=False)
    location = db.Column(db.String(192), nullable=False)
    musician_id = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.LargeBinary, default=None)
    rendered_cover_image = db.Column(db.Text, default=None)
    likes = db.Column(db.Integer, nullable=False, default=0) 

    def __init__(self, title, description, preferable_genres, location, instruments, musician_id):
        self.title = title
        self.description = description
        self.preferable_genres = preferable_genres
        self.location = location
        self.instruments = instruments
        self.musician_id = musician_id

    def get_id(self):
        return self.id  