from flask import request, render_template, session, redirect, url_for
from flask_login import login_user, logout_user
from flask_login.utils import login_required
from application import db
from application import app
from application.auth.forms import LoginForm, SigninForm
from application.auth.models import User
from application.util.security import encrypt_password, verify_password

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(email=form.email.data).first()

    if not user:
        return render_template("auth/login.html", form = form, error = "Either email or password is incorrect")

    if not(verify_password(form.password.data, user.password)):
        return render_template("auth/login.html", form = form, error = "No such email or password.")

    login_user(user)
    session['logged_in'] = True
    return redirect(url_for("profile"))

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    if session.get('logged_in'):
        del session['logged_in']
    return redirect(url_for("login"))

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("auth/signin.html", form = SigninForm(), users = None)

    form = SigninForm(request.form)
    users = User.query.all()
    emails_of_users = [user.email for user in users]
    if form.email.data in emails_of_users:
        return render_template("auth/signin.html", form = form, id_error = "This user has already signed in.")

    if not form.validate():
        return render_template("auth/signin.html", form = form)

    user = User(form.firstname.data, form.lastname.data, form.email.data, encrypt_password(form.password.data), form.instruments.data)

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("login"))