import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models import User
from website import db
from sqlalchemy import or_
from flask_login import login_required, current_user
import re

views = Blueprint('views', __name__)

@views.route("/", methods=["GET"])
@login_required
def index():

    return render_template("main.html", user=current_user)

