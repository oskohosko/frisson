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

    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")

    # Creating our database
    from .models import User
    create_database(app)

    # LoginManager stuff
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # Looking for a user and use function to load user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app



def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')