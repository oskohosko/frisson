"""
Our database model.
"""
from . import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    playlists = db.relationship("Playlists")

class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(150), unique=True)
    image= db.Column(db.String(150))
    uri = db.Column(db.String(150), unique=True)