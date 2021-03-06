from db import db
from flask import session
from util.security import (
    encrypt_password,
    get_timestamp,
    verify_password,
    random_num_with_n_digits,
)
import os


def get_user_by_email(email):
    sql = f"SELECT id, password, role FROM users WHERE email='{email}'"
    result = db.session.execute(sql)
    user = result.fetchone()
    return user


def login(email, password):
    user = get_user_by_email(email)
    if user == None:
        return False
    else:
        if verify_password(password, user.password):
            session[user.role] = True
            session["user_id"] = user.id
            session["csrf_token"] = random_num_with_n_digits(16)
            return True
        else:
            return False


def logout():
    if session.get("musician"):
        del session["musician"]
    if session.get("band"):
        del session["band"]
    if session.get("user_id"):
        del session["user_id"]
    if session.get("admin"):
        del session["admin"]
    if session.get("csrf"):
        del session["csrf"]


def signup(name, email, role, password):
    hash_value = encrypt_password(password)
    created_on = get_timestamp()
    try:
        sql = f"INSERT INTO users (name,email,role,password,created_on) VALUES ('{name}','{email}','{role}','{hash_value}','{created_on}')"
        db.session.execute(sql)
        db.session.commit()
    except:
        return False
    return True


if not get_user_by_email(os.getenv("ADMIN_EMAIL")):
    signup(
        os.getenv("ADMIN_NAME"),
        os.getenv("ADMIN_EMAIL"),
        "admin",
        os.getenv("ADMIN_PASSWD"),
    )
