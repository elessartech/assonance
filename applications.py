from db import db


def get_applications_by_publisher(publisher_id):
    result = db.session.execute(
        f"SELECT a.id, a.message, a.created_on, n.title as notification_title, u.name as user_name, u.email as user_email "
        f"FROM applications a LEFT JOIN notifications n ON n.id = a.notification_id "
        f"LEFT JOIN users u ON u.id = a.sender_id "
        f"WHERE n.publisher_id={publisher_id} AND n.hidden=0;"
    )
    return result.fetchall()

def get_application_by_id(id):
    result = db.session.execute(
        f"SELECT a.id, a.message, a.created_on, n.title as notification_title, u.name as user_name, u.email as user_email "
        f"FROM applications a LEFT JOIN notifications n ON n.id = a.notification_id "
        f"LEFT JOIN users u ON u.id = a.sender_id "
        f"WHERE a.id={id} AND n.hidden=0;"
    )
    return result.fetchone()

def save_application(message, sender_id, notification_id, created_on):
    query = f"INSERT INTO applications (message,sender_id,notification_id,created_on) VALUES ('{message}','{sender_id}','{notification_id}','{created_on}');"
    db.session.execute(query)
    db.session.commit()
    return True


def delete_application(id):
    sql = f"DELETE FROM applications WHERE id={id}"
    db.session.execute(sql)
    db.session.commit()
    return True
