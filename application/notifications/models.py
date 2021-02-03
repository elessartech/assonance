from application import db

class Notification(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

class NotificationForMusician(Notification):
    __tablename__ = 'notifications_for_musicians'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(192), nullable=False)
    instrument = db.Column(db.String(192), nullable=False)
    band_id = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.LargeBinary, default=None) 
    likes = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, title, description, instrument, band_id, cover_image):
        self.title = title
        self.description = description
        self.instrument = instrument
        self.band_id = band_id
        self.cover_image = cover_image

    def get_id(self):
        return self.id  

class NotificationForBand(Notification):
    __tablename__ = 'notifications_for_bands'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(128),  nullable=False)
    instrument = db.Column(db.String(192), nullable=False)
    description = db.Column(db.String(192), nullable=False)
    musician_id = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.LargeBinary, default=None)
    likes = db.Column(db.Integer, nullable=False, default=0) 

    def __init__(self, title, description, instrument, musician_id, cover_image):
        self.title = title
        self.description = description
        self.instrument = instrument
        self.musician_id = musician_id
        self.cover_image = cover_image

    def get_id(self):
        return self.id  