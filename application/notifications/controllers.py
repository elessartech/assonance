from flask import request, render_template, session, redirect, url_for
from application import app
from application import db
from application.notifications.forms import NewNotification
from application.notifications.models import Notification, Location, Genre, Instrument, get_highest_notif_id, get_all_notifications

@app.route('/notifications', methods=["GET"])
def notifications():
    all_notifications = get_all_notifications()
    return render_template("notifications/index.html", notifications = all_notifications) 

@app.route('/notifications/new-notification',  methods=["GET", "POST"])
def new_notification():
    if request.method == "GET":
            return render_template("notifications/new-notification.html", form=NewNotification())
    form=NewNotification(request.form)
    if not form.validate():
        return render_template("notifications/new-notification-band.html", form = form)
    new_notification_ds = Notification(form.title.data, form.description.data, form.publisher_id.data)
    db.session().add(new_notification_ds)
    db.session.commit()
    new_notification_id = int(get_highest_notif_id())
    objects_to_save = [new_notification_ds, Location(form.country.data, new_notification_id)]
    objects_to_save.append(Genre(form.genres.data, new_notification_id))
    objects_to_save.append(Instrument(form.instruments.data, new_notification_id))
    db.session().add_all(objects_to_save)
    db.session.commit()

    return redirect(url_for("notifications"))
