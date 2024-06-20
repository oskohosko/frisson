"""
Our database model.
"""
from . import db
from flask_login import UserMixin
# Beginning by just adding a User table

# Name, email, password - the basics to start
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))