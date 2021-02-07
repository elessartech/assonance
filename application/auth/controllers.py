from flask import request, render_template, session, redirect, url_for
from flask_login import login_user, logout_user
from flask_login.utils import login_required
from application import db
from application import app
from application.auth.forms import LoginForm, BandSignupForm, MusicianSignupForm
from application.auth.models import Band, Musician, Admin
from application.util.security import encrypt_password, verify_password

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())
    form = LoginForm(request.form)

    if form.role.data == "musician":
        model = Musician
        path_to_redir = "profile_musician"
    elif form.role.data == "band":
        model = Band
        path_to_redir = "profile_band"
    else:
        model = Admin
        path_to_redir = "profile_admin"
    
    user = model.query.filter_by(email=form.email.data).first()
    if not user:
        return render_template("auth/login.html", form = form, error = "No such email or password.")
    if not(verify_password(form.password.data, user.password)):
        return render_template("auth/login.html", form = form, error = "Either email or password is incorrect.")
    login_user(user)
    session[form.role.data] = True
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

@app.route("/signup-musician", methods=["GET", "POST"])
def signup_musician():
    if request.method == "GET":
        return render_template("auth/signup-musician.html", form = MusicianSignupForm(), users = None)
    form = MusicianSignupForm(request.form)
    musicians = Musician.query.all()
    emails_of_musicians = [musician.email for musician in musicians]
    if form.email.data in emails_of_musicians:
        return render_template("auth/signup-musician.html", form = form, id_error = "This user has already signed up.")
    if not form.validate():
        return render_template("auth/signup-musician.html", form = form)
    new_musician_user = Musician(form.firstname.data, form.lastname.data, form.email.data, encrypt_password(form.password.data), form.instruments.data, form.facebook.data, form.spotify.data, form.soundcloud.data)
    db.session().add(new_musician_user)
    db.session().commit()

    return redirect(url_for("login"))

@app.route("/signup-band", methods=["GET", "POST"])
def signup_band():
    if request.method == "GET":
        return render_template("auth/signup-band.html", form = BandSignupForm(), users = None)
    form = BandSignupForm(request.form)
    bands = Band.query.all()
    emails_of_bands = [band.email for band in bands]
    if form.email.data in emails_of_bands:
        return render_template("auth/signup-band.html", form = form, id_error = "This user has already signed up.")
    if not form.validate():
        return render_template("auth/signup-band.html", form = form)
    new_band_user = Band(form.title.data, form.email.data, encrypt_password(form.password.data), form.current_member_num.data, form.genres.data, form.facebook.data, form.spotify.data, form.soundcloud.data)
    db.session().add(new_band_user)
    db.session().commit()
    return redirect(url_for("login"))

@app.route('/profile-musician/<id>', methods=["GET"])
def profile_musician(id):
    musician = Musician.query.get(id)
    return render_template("musician/profile.html", musician=musician) 


@app.route('/profile-band/<id>', methods=["GET"])
def profile_band(id):
    band = Band.query.get(id)
    return render_template("band/profile.html", band=band) 

