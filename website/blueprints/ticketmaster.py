from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests
from flask_login import login_required, current_user

from CONFIG import API_KEY, DEFAULT_LINK, ROOT_URL, DEFAULT_COUNTRY, DEFAULT_CITY
from website import db
from website.models import Event

ticketmaster = Blueprint('ticketmaster', __name__)


@ticketmaster.route("/search_for_events",  methods=["GET", "POST"])
@login_required
def search_for_events():
    if request.method == "GET":
        return redirect(url_for('views.index'))
    if request.method == "POST":
        keyword_input = request.form.get('search_field')
        request_url = f"{ROOT_URL}{DEFAULT_LINK}events.json?countryCode={DEFAULT_COUNTRY}&city={DEFAULT_CITY}&keyword={keyword_input}&apikey={API_KEY}"

        try:

            response = requests.get(request_url)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            response_json = response.json()
            if "_embedded" in response_json:
                events = response_json["_embedded"]["events"]

            else:
                events = []
            return render_template("main.html", user=current_user, events=events)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors like 404, 500, etc.
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")  # Handle errors like DNS failure, refused connection.
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")  # Handle timeouts like slow connection problems.
        except requests.exceptions.RequestException as req_err:
            print(f"Error during request: {req_err}")  # Handle any request-related errors.
        except Exception as e:
            print(f"An error occurred: {e}")  # Handle other possible errors.


@ticketmaster.route("/add_event",  methods=["POST"])
@login_required
def add_event():
    if request.method == "POST":
        event_id = request.form.get('event_id')
        event_name = request.form.get('event_name')
        event_url = request.form.get('event_url')
        event_img_url = request.form.get('event_img_url')
        event = Event.query.filter_by(event_id=event_id).first()
        if event:
            flash('Event already added.', category='error')
        else:
            new_user = Event(event_id=event_id, name=event_name, url=event_url, img_url=event_img_url, event_category=2)
            db.session.add(new_user)
            db.session.commit()
    return redirect(url_for('views.index'))