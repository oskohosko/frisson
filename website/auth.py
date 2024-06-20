"""
User Authentication.
"""
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Users
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import re
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def sign_up():

    # When someone submits the sign up form
    if request.method == "POST":
        # Grabbing all of the fields we need
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        conf_password = request.form.get("confirm_password")

        # Firstly going to handle errors

        # Using a regular expression to handle emails
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Now checking if a user exists
        user = Users.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif not re.match(email_pattern, email):
            flash("Not a valid email address.", category="error")
        elif password != conf_password:
            flash("Passwords don't match", category="error")
        elif len(password) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            # Now we add the user to the database.
            new_user = Users(email=email, name=name, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash("Signed up successfully!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)