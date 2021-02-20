from db import db

def get_highest_notification_id():
    result = db.session.execute('SELECT id FROM notifications ORDER BY id DESC LIMIT 1;')
    return result.fetchone()[0]

def get_number_of_notifications():
    result = db.session.execute('SELECT COUNT(*) FROM notifications;')
    return result.fetchone()[0]

def get_all_notifications():
    result = db.session.execute(
    f'SELECT n.id, n.title, n.description, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, l.name as location ' 
    f'FROM notifications n ' 
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id;')
    return result.fetchall()

def get_notifications_by_user_id(id):
    result = db.session.execute(
    f'SELECT n.id, n.title, n.description, n.date_created as date_created, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, '
    f'l.country as country FROM notifications n '
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id '
    f'WHERE n.publisher_id={id};')
    return result.fetchall()

def get_notification_by_notification_id(id):
    result = db.session.execute(
    f'SELECT n.id, n.title, n.description, n.date_created as date_created, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, '
    f'l.country as country FROM notifications n '
    f'LEFT JOIN users u ON u.id = n.publisher_id '
    f'LEFT JOIN genres g ON g.notification_id = n.id '
    f'LEFT JOIN instruments i ON i.notification_id = n.id '
    f'LEFT JOIN locations l ON l.notification_id = n.id '
    f'WHERE n.id={id};')
    return result.fetchone()

def save_notification(title, description, publisher_id):
    query = 'INSERT INTO notifications (title,description,publisher_id) VALUES (:title,:description,:publisher_id) RETURNING id'
    result = db.session.execute(query, {"title":title,"description":description,"publisher_id":publisher_id})
    db.session.commit()
    return True

def save_location(name, notification_id):
    query = 'INSERT INTO locations (name,notification_id) VALUES (:name,:notification_id) RETURNING id'
    result = db.session.execute(query, {"name":name,"notification_id":notification_id})
    db.session.commit()
    return True

def save_instrument(name, notification_id):
    query = 'INSERT INTO instruments (name,notification_id) VALUES (:name,:notification_id) RETURNING id'
    result = db.session.execute(query, {"name":name,"notification_id":notification_id})
    db.session.commit()
    return True

def save_genre(name, notification_id):
    query = 'INSERT INTO genres (name,notification_id) VALUES (:name,:notification_id) RETURNING id'
    result = db.session.execute(query, {"name":name,"notification_id":notification_id})
    db.session.commit()
    return True