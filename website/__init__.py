"""
Let's begin by initialising our app so we can do stuff with it.
"""
# Importing stuff I think will be important
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
from dotenv import load_dotenv

# Setting up our database
db = SQLAlchemy()
DB_NAME = "database.db"

# For env variables
load_dotenv()

# And now creating our app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    # Using SQLite for local projects
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # No background stuff going on
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
