from flask.globals import session
from app import app
from flask import render_template, request, redirect
import notifications, users
from util.data import get_locations, get_instruments, get_genres

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(err):
    return render_template('404.html'), 404

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if users.login(email, password):
            return redirect("/notifications")
        else:
            return render_template("auth/login.html", error="Wrong email or password")

@app.route("/logout", methods=["GET","POST"])
def logout():
    users.logout()
    return redirect("/login")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html")
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password != confirm_password:
            return render_template("auth/signup.html", error="Passwords do not match")
        if users.signup(name,email,role,password):      
            return redirect("/login")
        else:
            return render_template("auth/signup.html", error="Registration did not succeed")

@app.route("/notifications", methods=["GET", "POST"])
def show_notifications():
    if request.method == "GET":
        all_notifications = notifications.get_all_notifications()
        return render_template("notifications/index.html", notifications=all_notifications)
    
@app.route("/new-notification", methods=["GET", "POST"])
def new_notification():
    if request.method == "GET":
        locations = get_locations()
        genres = get_genres()
        instruments = get_instruments()
        return render_template("notifications/new-notification.html", locations=locations, genres=genres, instruments=instruments)
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        publisher_id = request.form["publisher_id"]
        location = request.form["location"]
        genre = request.form["genre"]
        instrument = request.form["instrument"]
        if notifications.save_notification(title, description, publisher_id):
            last_notification_id = notifications.get_highest_notification_id()
            saved_location = notifications.save_location(location, last_notification_id)
            saved_genre = notifications.save_genre(genre, last_notification_id)
            saved_instrument = notifications.save_instrument(instrument, last_notification_id)
            if saved_location and saved_genre and saved_instrument:
                return redirect("/notifications")
            else:
                return render_template("notifications/new-notification.html", error="Could not create new notification")
        else:
            return render_template("notifications/new-notification.html", error="Could not create new notification")
    
@app.route('/notification/<notification_id>',  methods=["GET"])
def show_single_notificaiton(notification_id):
    if request.method == "GET":
        notification_by_notification_id = notifications.get_notification_by_notification_id(notification_id)
        return render_template("notifications/notification.html", notification = notification_by_notification_id)
