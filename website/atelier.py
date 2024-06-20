from flask import Blueprint, render_template
from flask_login import current_user, login_required

atelier_bp = Blueprint("atelier", __name__)

@atelier_bp.route("/audio-atelier")
@login_required
def atelier():
    return render_template('atelier.html', user=current_user)