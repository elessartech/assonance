from app import app
from flask import render_template, request, redirect, session, abort
import notifications, users, applications
from util.resources import get_locations, get_instruments, get_genres
from util.security import get_timestamp

locations = get_locations()
genres = get_genres()
instruments = get_instruments()


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found(err):
    return render_template("404.html"), 404


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if not email or not password:
            return render_template(
                "auth/login.html", error="Please, fill all the inputs."
            )
        if users.login(email, password):
            return redirect("/notifications")
        else:
            return render_template("auth/login.html", error="Wrong email or password")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    users.logout()
    return redirect("/login")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html")
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if not name or not email or not role or not password or not confirm_password:
            return render_template(
                "auth/signup.html", error="Please, fill all the inputs."
            )
        if password != confirm_password:
            return render_template("auth/signup.html", error="Passwords do not match")
        if users.signup(name, email, role, password):
            return redirect("/login")
        else:
            return render_template(
                "auth/signup.html", error="Registration did not succeed"
            )


@app.route("/notifications", methods=["GET"])
def show_notifications():
    if request.method == "GET":
        filter = request.args.get("filter")
        if filter:
            filtered_notification = (
                notifications.get_all_notifications_grouped_by_filter(filter)
            )
            return render_template(
                "notifications/notifications.html", notifications=filtered_notification
            )
        else:
            all_notifications = notifications.get_all_notifications()
            return render_template(
                "notifications/notifications.html", notifications=all_notifications
            )


@app.route("/my-notifications/<user_id>", methods=["GET"])
def show_user_notifications(user_id):
    if request.method == "GET":
        if session["user_id"] != int(user_id):
            abort(403)
        user_notifications = notifications.get_notifications_by_user_id(user_id)
        return render_template(
            "notifications/my-notifications.html", notifications=user_notifications
        )


@app.route("/new-notification", methods=["GET", "POST"])
def new_notification():
    if request.method == "GET":
        if not session.get("user_id"):
            abort(403)
        return render_template(
            "notifications/new-notification.html",
            locations=locations,
            genres=genres,
            instruments=instruments,
        )
    if request.method == "POST":
        if int(session["csrf_token"]) != int(request.form["csrf_token"]):
            abort(403)
        title = request.form["title"]
        description = request.form["description"]
        publisher_id = request.form["publisher_id"]
        location = request.form["location"]
        genre = request.form["genre"]
        instrument = request.form["instrument"]
        if (
            not title
            or not description
            or not publisher_id
            or not location
            or not genre
            or not instrument
        ):
            return render_template(
                "notifications/new-notification.html",
                error="Please, provide all the required information",
                locations=locations,
                genres=genres,
                instruments=instruments,
            )
        created_on = get_timestamp()
        if notifications.save_notification(
            title, description, publisher_id, created_on
        ):
            last_notification_id = notifications.get_highest_notification_id()
            saved_location = notifications.save_location(location, last_notification_id)
            saved_genre = notifications.save_genre(genre, last_notification_id)
            saved_instrument = notifications.save_instrument(
                instrument, last_notification_id
            )
            if saved_location and saved_genre and saved_instrument:
                return redirect("/notifications")
            else:
                return render_template(
                    "notifications/new-notification.html",
                    error="Could not create new notification",
                    locations=locations,
                    genres=genres,
                    instruments=instruments,
                )
        else:
            return render_template(
                "notifications/new-notification.html",
                error="Could not create new notification",
                locations=locations,
                genres=genres,
                instruments=instruments,
            )


@app.route("/notification/<notification_id>", methods=["GET"])
def show_single_notificaiton(notification_id):
    if request.method == "GET":
        notification_by_notification_id = (
            notifications.get_notification_by_notification_id(notification_id)
        )
        return render_template(
            "notifications/notification.html",
            notification=notification_by_notification_id,
        )


@app.route("/delete-notification", methods=["POST"])
def delete_single_notificaiton():
    if request.method == "POST":
        if session["csrf_token"] != int(request.form["csrf_token"]):
            abort(403)
        notification_id = request.form["notification_id"]
        was_notification_deleted = notifications.delete_notification(notification_id)
        if was_notification_deleted:
            return redirect("/notifications")
        else:
            return False


@app.route("/edit-notification/<notification_id>", methods=["GET", "POST"])
def edit_single_notificaiton(notification_id):
    notification_to_edit = notifications.get_notification_by_notification_id(
        notification_id
    )
    if request.method == "GET":
        if not session.get("admin"):
            abort(403)
        if notification_to_edit:
            return render_template(
                "notifications/edit-notification.html",
                notification=notification_to_edit,
                locations=locations,
                genres=genres,
                instruments=instruments,
            )
        else:
            return False
    if request.method == "POST":
        if int(session["csrf_token"]) != int(request.form["csrf_token"]):
            abort(403)
        title = request.form["title"]
        description = request.form["description"]
        location = request.form["location"]
        genre = request.form["genre"]
        instrument = request.form["instrument"]
        if not title or not description or not location or not genre or not instrument:
            return render_template(
                "notifications/new-notification.html",
                error="Could not update the notification",
                notification=notification_to_edit,
                locations=locations,
                genres=genres,
                instruments=instruments,
            )
        if notifications.update_notification(notification_id, title, description):
            updated_location = notifications.update_location(location, notification_id)
            updated_genre = notifications.update_genre(genre, notification_id)
            updated_instrument = notifications.update_instrument(
                instrument, notification_id
            )
            if updated_location and updated_genre and updated_instrument:
                return redirect("/notifications")
            else:
                return render_template(
                    "notifications/new-notification.html",
                    error="Could not update the notification",
                    notification=notification_to_edit,
                    locations=locations,
                    genres=genres,
                    instruments=instruments,
                )
        else:
            return render_template(
                "notifications/new-notification.html",
                error="Could not update the notification",
                notification=notification_to_edit,
                locations=locations,
                genres=genres,
                instruments=instruments,
            )


@app.route("/hide-notification", methods=["POST"])
def hide_notification_visibility():
    if request.method == "POST":
        if session["csrf_token"] != int(request.form["csrf_token"]):
            abort(403)
        notification_id = request.form["notification_id"]
        was_notification_hidden = notifications.hide_notification(notification_id)
        if was_notification_hidden:
            return redirect("/my-notifications/" + str(session["user_id"]))
        else:
            return False


@app.route("/unhide-notification", methods=["POST"])
def unhide_notification_visibility():
    if request.method == "POST":
        if session["csrf_token"] != int(request.form["csrf_token"]):
            abort(403)
        notification_id = request.form["notification_id"]
        was_notification_unhidden = notifications.unhide_notification(notification_id)
        if was_notification_unhidden:
            return redirect("/my-notifications/" + str(session["user_id"]))
        else:
            return False


@app.route("/applications/<user_id>", methods=["GET"])
def show_applications(user_id):
    if request.method == "GET":
        if session["user_id"] != int(user_id):
            abort(403)
        received_applications = applications.get_applications_by_publisher(user_id)
        return render_template(
            "applications/applications.html", applications=received_applications
        )


@app.route("/application/<user_id>/<application_id>", methods=["GET"])
def show_single_application(user_id, application_id):
    if request.method == "GET":
        if session["user_id"] != int(user_id):
            abort(403)
        received_application = applications.get_application_by_id(application_id)
        return render_template(
            "applications/application.html", application=received_application
        )


@app.route("/apply/<notification_id>", methods=["GET", "POST"])
def apply_for_notification(notification_id):
    notification_to_apply = notifications.get_notification_by_notification_id(
        notification_id
    )
    if request.method == "GET":
        if not session.get("user_id"):
            abort(403)
        if int(session["user_id"]) == int(notification_to_apply.publisher_id):
            abort(403)
        return render_template(
            "applications/apply-form.html", notification=notification_to_apply
        )
    if request.method == "POST":
        if int(session["csrf_token"]) != int(request.form["csrf_token"]):
            abort(403)
        message = request.form["message"]
        if not message:
            return render_template(
                "applications/apply-form.html",
                error="Please, enter your message.",
                notification=notification_to_apply,
            )
        sender_id = request.form["user_id"]
        created_on = get_timestamp()
        if applications.save_application(
            message, sender_id, notification_id, created_on
        ):
            return redirect("/notifications")
        else:
            return render_template(
                "applications/apply-form.html",
                error="Something went wrong. Please, try again.",
                notification=notification_to_apply,
            )


@app.route("/delete-application", methods=["POST"])
def delete_single_application():
    if request.method == "POST":
        if session["csrf_token"] != int(request.form["csrf_token"]):
            abort(403)
        application_id = request.form["application_id"]
        was_application_deleted = applications.delete_application(application_id)
        if was_application_deleted:
            return redirect("/applications/" + str(session["user_id"]))
        else:
            return False
