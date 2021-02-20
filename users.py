from db import db
from flask import session
from util.security import encrypt_password, verify_password, random_num_with_n_digits

def login(email, password):
    sql = "SELECT id, password, role FROM users WHERE email=:email"
    result = db.session.execute(sql, {"email":email})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if verify_password(password, user.password):
            print(user)
            session[user.role] = True
            session["user_id"] = user.id
            session["csrf_token"] = random_num_with_n_digits(16)
            return True
        else:
            return False

def logout():
    if session.get('musician'):
        del session['musician']
    if session.get('band'):
        del session['band']
    if session.get('admin'):
        del session['admin']
    if session.get('csrf'):
        del session['csrf']

def signup(name,email,role,password):
    hash_value = encrypt_password(password)
    try:
        sql = "INSERT INTO users (name,email,role,password) VALUES (:name,:email,:role,:password)"
        db.session.execute(sql, {"name":name,"email":email,"role":role,"password":hash_value})
        db.session.commit()
    except:
        return False
    return True