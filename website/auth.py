"""
User Authentication.
"""
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template

load_dotenv()

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    return render_template("signup.html")