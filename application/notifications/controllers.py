from flask import request, render_template, redirect, url_for
from application import app
from application import db
from application.notifications.forms import NewNotification, FilterNotifications
from application.notifications.models import Notification, Location, Genre, Instrument, get_highest_notification_id, get_all_notifications, get_notifications_by_user_id, get_notification_by_notification_id
from sqlalchemy.sql import text


@app.route('/notifications', methods=["GET", "POST"])
def notifications():
    if request.method == "GET":
        form = FilterNotifications()
        all_notifications = Notification.query.join(Location).add_columns(Location.country).join(Genre).add_columns(Genre.genre_name).join(Instrument).add_columns(Instrument.instrument_name).all()
        return render_template("notifications/index.html", notifications = all_notifications, form = form) 
    form=FilterNotifications(request.form)
    if not form.validate():
        return render_template("notifications/index.html", form = form)
    if form.show.data == "my notifications":
        fetched_notifications_query = Notification.query.join(Location).add_columns(Location.country).join(Genre).add_columns(Genre.genre_name).join(Instrument).add_columns(Instrument.instrument_name).filter(text(f'notifications.publisher_id={form.publisher_id.data}')).group_by(text(f'notifications.id'))
    else:
        fetched_notifications_query = Notification.query.join(Location).add_columns(Location.country).join(Genre).add_columns(Genre.genre_name).join(Instrument).add_columns(Instrument.instrument_name).group_by(text(f'notifications.id'))
    if form.filter.data != "no filter":
        filtered_notifications = fetched_notifications_query.all()
    else:
        filtered_notifications = fetched_notifications_query.all()
    return render_template("notifications/index.html", notifications = filtered_notifications, form = form)

@app.route('/new-notification',  methods=["GET", "POST"])
def new_notification():
    if request.method == "GET":
            return render_template("notifications/new-notification.html", form=NewNotification())
    form=NewNotification(request.form)
    if not form.validate():
        return render_template("notifications/new-notification.html", form = form)
    new_notification_dataset = Notification(form.title.data, form.description.data, form.publisher_id.data)
    db.session().add(new_notification_dataset)
    db.session.commit()
    new_notification_id = int(get_highest_notification_id())
    objects_to_save = [Location(form.country.data, new_notification_id), Genre(form.genre.data, new_notification_id), Instrument(form.instrument.data, new_notification_id)]
    db.session().add_all(objects_to_save)
    db.session.commit()
    return redirect(url_for("notifications"))

@app.route('/my-notifications/<user_id>',  methods=["GET"])
def my_notifications(user_id):
    notifications_by_id = get_notifications_by_user_id(user_id)
    return render_template("notifications/my-notifications.html", notifications = notifications_by_id) 

@app.route('/notification/<notification_id>',  methods=["GET"])
def notification(notification_id):
    notification = get_notification_by_notification_id(notification_id)
    return render_template("notifications/notification.html", notification = notification) 
