from db import db


def get_highest_notification_id():
    result = db.session.execute(
        f"SELECT id FROM notifications ORDER BY id DESC LIMIT 1;"
    )
    return result.fetchone()[0]


def get_number_of_notifications():
    result = db.session.execute(f"SELECT COUNT(*) FROM notifications;")
    return result.fetchone()[0]


def get_notification_visibility(id):
    result = db.session.execute(f"SELECT hidden FROM notifications WHERE id={id};")
    return result.fetchone()[0]


def get_all_notifications():
    result = db.session.execute(
        f"SELECT n.id, n.hidden, n.created_on, n.title, n.description, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, l.name as location, substr(n.created_on, 0, 11) as created_on "
        f"FROM notifications n "
        f"LEFT JOIN users u ON u.id = n.publisher_id "
        f"LEFT JOIN genres g ON g.notification_id = n.id "
        f"LEFT JOIN instruments i ON i.notification_id = n.id "
        f"LEFT JOIN locations l ON l.notification_id = n.id "
        f"WHERE n.hidden=0"
        f"ORDER BY n.created_on DESC"
    )
    return result.fetchall()


def get_all_notifications_grouped_by_filter(filter):
    result = db.session.execute(
        f"SELECT n.id, n.title as title, n.description, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, l.name as location, substr(n.created_on, 0, 11) as created_on "
        f"FROM notifications n "
        f"LEFT JOIN users u ON u.id = n.publisher_id "
        f"LEFT JOIN genres g ON g.notification_id = n.id "
        f"LEFT JOIN instruments i ON i.notification_id = n.id "
        f"LEFT JOIN locations l ON l.notification_id = n.id "
        f"WHERE n.hidden=0 "
        f"ORDER BY {filter};"
    )
    return result.fetchall()


def get_notifications_by_user_id(id):
    result = db.session.execute(
        f"SELECT n.id, n.title, n.description, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, "
        f"l.name as location, n.hidden as hidden, substr(n.created_on, 0, 11) as created_on FROM notifications n "
        f"LEFT JOIN users u ON u.id = n.publisher_id "
        f"LEFT JOIN genres g ON g.notification_id = n.id "
        f"LEFT JOIN instruments i ON i.notification_id = n.id "
        f"LEFT JOIN locations l ON l.notification_id = n.id "
        f"WHERE n.publisher_id={id};"
    )
    return result.fetchall()


def get_notification_by_notification_id(id):
    result = db.session.execute(
        f"SELECT n.id, n.title, n.description, n.publisher_id, u.name as publisher_name, u.role as publisher_role, g.name as genre, i.name as instrument, "
        f"l.name as location, substr(n.created_on, 0, 11) as created_on FROM notifications n "
        f"LEFT JOIN users u ON u.id = n.publisher_id "
        f"LEFT JOIN genres g ON g.notification_id = n.id "
        f"LEFT JOIN instruments i ON i.notification_id = n.id "
        f"LEFT JOIN locations l ON l.notification_id = n.id "
        f"WHERE n.id={id};"
    )
    return result.fetchone()


def save_notification(title, description, publisher_id, created_on):
    query = f"INSERT INTO notifications (title,description,publisher_id,created_on) VALUES ('{title}','{description}','{publisher_id}','{created_on}');"
    db.session.execute(query)
    db.session.commit()
    return True


def save_location(name, notification_id):
    query = f"INSERT INTO locations (name,notification_id) VALUES ('{name}','{notification_id}');"
    result = db.session.execute(query)
    db.session.commit()
    return True


def save_instrument(name, notification_id):
    query = f"INSERT INTO instruments (name,notification_id) VALUES ('{name}','{notification_id}');"
    db.session.execute(query)
    db.session.commit()
    return True


def save_genre(name, notification_id):
    query = f"INSERT INTO genres (name,notification_id) VALUES ('{name}','{notification_id}');"
    db.session.execute(query)
    db.session.commit()
    return True


def delete_notification(id):
    sql = f"DELETE FROM notifications WHERE id={id}"
    db.session.execute(sql)
    db.session.commit()
    return True


def update_notification(id, title, description):
    query = f"UPDATE notifications SET title='{title}', description='{description}' WHERE id={id};"
    db.session.execute(query)
    db.session.commit()
    return True


def update_location(name, notification_id):
    query = (
        f"UPDATE locations SET name='{name}' WHERE notification_id={notification_id};"
    )
    db.session.execute(query)
    db.session.commit()
    return True


def update_instrument(name, notification_id):
    query = (
        f"UPDATE instruments SET name='{name}' WHERE notification_id={notification_id};"
    )
    db.session.execute(query)
    db.session.commit()
    return True


def update_genre(name, notification_id):
    query = f"UPDATE genres SET name='{name}' WHERE notification_id={notification_id};"
    db.session.execute(query)
    db.session.commit()
    return True


def hide_notification(id):
    query = f"UPDATE notifications SET hidden='1' WHERE id={id};"
    db.session.execute(query)
    db.session.commit()
    return True


def unhide_notification(id):
    query = f"UPDATE notifications SET hidden='0' WHERE id={id};"
    db.session.execute(query)
    db.session.commit()
    return True
