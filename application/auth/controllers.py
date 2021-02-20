from flask import request, render_template, session, redirect, url_for
from flask_login import login_user, logout_user
from flask_login.utils import login_required
from application import db
from application import app
from application.auth.forms import LoginForm, SignupForm
from application.auth.models import User
from application.util.security import encrypt_password, verify_password
import os

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())
    form = LoginForm(request.form)
    user = User.query.filter_by(email=form.email.data).first()
    if not user:
        return render_template("auth/login.html", form = form, error = "No such email or password.")
    if not(verify_password(form.password.data, user.password)):
        return render_template("auth/login.html", form = form, error = "Either email or password is incorrect.")
    login_user(user)
    path_to_redir = "user_profile"
    session[user.role] = True
    return redirect(url_for(path_to_redir, id=user.id))

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    if session.get('musician'):
        del session['musician']
    if session.get('band'):
        del session['band']
    if session.get('admin'):
        del session['admin']
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup_band():
    if request.method == "GET":
        return render_template("auth/signup.html", form = SignupForm(), users = None)
    form = SignupForm(request.form)
    users = User.query.all()
    emails_of_users = [user.email for user in users]
    if form.password.data != form.confirm_password.data:
         return render_template("auth/signup.html", form = form, error = "Passwords do not match!")
    if form.email.data in emails_of_users:
        return render_template("auth/signup.html", form = form, error = "This user has already signed up!")
    if not form.validate():
        return render_template("auth/signup.html", form = form, error="Something went wrong. Try again, please!")
    new_user = User(form.name.data, form.email.data, form.role.data, encrypt_password(form.password.data))
    db.session().add(new_user)
    db.session().commit()
    return redirect(url_for("login"))

@app.route('/user/profile/<id>', methods=["GET"])
def user_profile(id):
    user = User.query.get(id)
    return render_template("profile/profile.html", user=user) 

