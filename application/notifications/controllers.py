from flask import request, render_template, session, redirect, url_for
from application import app
from application import db
from application.notifications.forms import NewNotification
from application.notifications.models import Notification

@app.route('/notifications', methods=["GET"])
def notifications():
    notifications_to_show = Notification.query.all()
    return render_template("notifications/index.html", notifications=notifications_to_show) 

@app.route('/notifications/new-notification',  methods=["GET", "POST"])
def new_notification():
    if request.method == "GET":
            return render_template("notifications/new-notification.html", form=NewNotification())
    form  = NewNotification(request.form)
    model = Notification
    if session.get('musician'):
        posted_by = "musician"
    elif session.get('band'):
        posted_by = "band"
    else:
        return render_template("notifications/new-notification-band.html")
    if not form.validate():
        return render_template("notifications/new-notification-band.html", form = form)
    new_notification_dataset = model(form.title.data, form.description.data, form.preferable_genres.data, form.location.data, form.instruments.data, form.publisher_id.data, posted_by)
    db.session().add(new_notification_dataset)
    db.session().commit()

    return redirect(url_for("notifications"))
