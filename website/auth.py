"""
User Authentication.
"""
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

load_dotenv()

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def sign_up():

    return render_template("signup.html", user=current_user)