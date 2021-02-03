from flask import request, render_template, session, redirect, url_for
from application import app

@app.route('/notifications', methods=["GET"])
def profile():
    return render_template("notifications/index.html") 