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

    names = db.Column(db.ARRAY(db.String(128)), nullable = False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, names, notification_id):
        self.names = names
        self.notification_id = notification_id


class Genre(Base):
    __tablename__ = 'genres'

    names = db.Column(db.ARRAY(db.String(128)), nullable = False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, names, notification_id):
        self.names = names
        self.notification_id = notification_id

class Location(Base):
    __tablename__ = 'locations'

    country = db.Column(db.String(128), nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)

    def __init__(self, country, notification_id):
        self.country = country
        self.notification_id = notification_id


def get_highest_notif_id():
    result = db.engine.execute('SELECT id FROM notifications ORDER BY id DESC LIMIT 1;')
    return result.fetchone()[0]

def get_num_of_notifs():
    result = db.engine.execute('SELECT COUNT(*) FROM notifications;')
    return result.fetchone()[0]

def get_all_notifications():
    result = db.engine.execute(
    f'SELECT n.id, n.title, n.description, n.likes, n.date_created as date_created, u.name as publisher_name, u.role as publisher_role, g.names as genres, i.names as instruments, '
    f'l.country as country FROM notifications n '
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id;')
    return result.fetchall()