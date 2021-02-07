from application import db

class NotificationBase(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

    def get_id(self):
        return self.id

class Notification(NotificationBase):
    __tablename__ = 'notifications'

    title = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(192), nullable=False)
    preferable_genres = db.Column(db.String(192), nullable=False)
    location = db.Column(db.String(192), nullable=False)
    instruments = db.Column(db.String(192), nullable=False)
    publisher_id = db.Column(db.Integer, nullable=False) # either musician or band id
    posted_by = db.Column(db.String(128), nullable=False) # either musician or band
    cover_image = db.Column(db.LargeBinary, default=None) 
    rendered_cover_image = db.Column(db.Text, default=None)
    likes = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, title, description, preferable_genres, location, instruments, publisher_id, posted_by):
        self.title = title
        self.description = description
        self.preferable_genres = preferable_genres
        self.location = location
        self.instruments = instruments
        self.publisher_id = publisher_id
        self.posted_by = posted_by
