from flask import request, render_template, session, redirect, url_for
from application import app
from application import db
from application.notifications.forms import NotificationForFindingMusicianForm, NotificationForFindingBandForm
from application.notifications.models import NotificationForFindingBand, NotificationForFindingMusician
from application.util.security import render_picture

@app.route('/notifications', methods=["GET"])
def notifications(): # if musician - for musicians, band - for bands, else - show everything
    all_notifications = NotificationForFindingMusician.query.all()
    return render_template("notifications/index.html", notifications=all_notifications) 

@app.route('/notifications/new-notification',  methods=["GET", "POST"])
def new_notification():
    if request.method == "GET":
        if session.get('musician'):
            return render_template("notifications/new-notification.html", form=NotificationForFindingBandForm())
        elif session.get('band'):
            return render_template("notifications/new-notification.html", form=NotificationForFindingMusicianForm())
    if session.get('musician'):
        form = NotificationForFindingBandForm(request.form)
        model = NotificationForFindingBand
        user_id = form.musician_id.data
    elif session.get('band'):
        form = NotificationForFindingMusicianForm(request.form)
        model = NotificationForFindingMusician
        user_id = form.band_id.data
    else:
        return render_template("notifications/new-notification-band.html")
    if not form.validate():
        return render_template("notifications/new-notification-band.html", form = form)
    new_notification_for_finding_musician = model(form.title.data, form.description.data, form.preferable_genres.data, form.location.data, form.instruments.data, user_id)
    db.session().add(new_notification_for_finding_musician)
    db.session().commit()

    return redirect(url_for("notifications"))
