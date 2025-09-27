from flask import Blueprint, render_template, session
from backend.data_logic.userdata import get_user

general_bp = Blueprint('general_routes', __name__)

@general_bp.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html', user_name=get_user(session['user_id']).name)

    return render_template('index.html')