from application import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

class Notification(Base):
    __tablename__ = 'notifications'

    title = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(192), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    likes = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, title, description, publisher_id):
        self.title = title
        self.description = description
        self.publisher_id = publisher_id

    def get_id(self):
        return self.id


class Instrument(Base):
    __tablename__ = 'instruments'

    name = db.Column(db.String(128),  nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, name, notification_id):
        self.name = name
        self.notification_id = notification_id


class Genre(Base):
    __tablename__ = 'genres'

    name = db.Column(db.String(128),  nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, name, notification_id):
        self.name = name
        self.notification_id = notification_id

class Location(Base):
    __tablename__ = 'locations'

    country = db.Column(db.String(128), nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, country, notification_id):
        self.country = country
        self.notification_id = notification_id


def get_num_of_all_notifs():
    result = db.engine.execute('SELECT COUNT(*) FROM notifications')
    return result.fetchall()[0][0]

def get_all_notifications():
    result = db.engine.execute('SELECT * FROM notifications;')
    
    return result.fetchall()