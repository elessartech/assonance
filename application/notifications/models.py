from application import db
from application.models import Base

class Notification(Base):
    __tablename__ = 'notifications'

    title = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(192), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, publisher_id):
        self.title = title
        self.description = description
        self.publisher_id = publisher_id

class Instrument(Base):
    __tablename__ = 'instruments'

    instrument_name = db.Column(db.String(128), nullable = False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, instrument_name, notification_id):
        self.instrument_name = instrument_name
        self.notification_id = notification_id

class Genre(Base):
    __tablename__ = 'genres'

    genre_name = db.Column(db.String(128), nullable = False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, genre_name, notification_id):
        self.genre_name = genre_name
        self.notification_id = notification_id

class Location(Base):
    __tablename__ = 'locations'

    country = db.Column(db.String(128), nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, country, notification_id):
        self.country = country
        self.notification_id = notification_id

def get_highest_notification_id():
    result = db.engine.execute('SELECT id FROM notifications ORDER BY id DESC LIMIT 1;')
    return result.fetchone()[0]

def get_number_of_notifications():
    result = db.engine.execute('SELECT COUNT(*) FROM notifications;')
    return result.fetchone()[0]

def get_all_notifications():
    result = db.engine.execute(
    f'SELECT n.id, n.title, n.description, n.date_created as date_created, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, '
    f'l.country as country FROM notifications n '
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id;')
    return result.fetchall()

def get_notifications_by_user_id(id):
    result = db.engine.execute(
    f'SELECT n.id, n.title, n.description, n.date_created as date_created, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, '
    f'l.country as country FROM notifications n '
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id '
    f'WHERE n.publisher_id={id};')
    return result.fetchall()

def get_notification_by_notification_id(id):
    result = db.engine.execute(
    f'SELECT n.id, n.title, n.description, n.date_created as date_created, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, '
    f'l.country as country FROM notifications n '
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id '
    f'WHERE n.id={id};')
    return result.fetchone()