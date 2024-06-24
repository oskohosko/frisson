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

    # When someone submits one of the forms
    if request.method == "POST":

        form_type = request.form.get("form-type")

        # User has hit signup
        if form_type == "signup":
            
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
        
        elif form_type == "login":
            email = request.form.get("email")
            password = request.form.get("password")

            user = Users.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in successfully!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for("views.home"))
                else:
                    flash("Incorrect password, please try again.", category="error")
            else:
                flash("Email does not exist.", category="error")
        else:
            flash("Oops", category="error")

    return render_template("signup.html", active="signup", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))