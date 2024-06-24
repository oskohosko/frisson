from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
import re
import os
from dotenv import load_dotenv

from playlist_analysis import analyse_playlist


atelier_bp = Blueprint("atelier", __name__)

@atelier_bp.route("/audio-atelier", methods=["GET", "POST"])
@login_required
def atelier():

    # User has submitted a playlist. So we get the URI
    if request.method == "POST":
        playlist_uri = request.form.get("playlist_uri")

        # Regular expression to match playlist URIs against
        uri_re = r"spotify:playlist:[a-zA-Z0-9]+"


    return render_template('atelier.html', active="atelier", user=current_user)