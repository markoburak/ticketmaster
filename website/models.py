from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    created_date = db.Column(db.Date(), default=func.now())
    event_category = db.relationship('EventCategory')

class EventCategory(db.Model):

    __tablename__ = "EventCategory"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), default='Default')
    created_date = db.Column(db.Date(), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event = db.relationship('Event')


class Event(db.Model):

    __tablename__ = "Event"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(50))
    name = db.Column(db.String(250))
    url = db.Column(db.String(400))
    img_url = db.Column(db.String(400))
    created_date = db.Column(db.Date(), default=func.now())
    event_category = db.Column(db.Integer, db.ForeignKey('EventCategory.id'))