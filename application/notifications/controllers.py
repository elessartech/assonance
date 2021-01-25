from flask import request, render_template, session, redirect, url_for
from application import app

@app.route('/profile', methods=["GET"])
def profile():
    return render_template("musician/profile.html") 