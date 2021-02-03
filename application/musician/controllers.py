from flask import request, render_template, session, redirect, url_for
from application import app

@app.route('/profile-musician', methods=["GET"])
def profile_musician():
    return render_template("musician/profile.html") 