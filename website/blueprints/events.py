from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests
from flask_login import login_required, current_user

from CONFIG import API_KEY, DEFAULT_LINK, ROOT_URL, DEFAULT_COUNTRY, DEFAULT_CITY
from website import db
from website.models import Event, EventCategory

events = Blueprint('events', __name__)

@events.route("/events",  methods=["GET"])
@login_required
def get_events():
    if request.method == "GET":

        user_events = Event.query.all()
        user_categories = EventCategory.query.all()
        return render_template("events.html", user=current_user, user_events=user_events, user_categories=user_categories)