from backend.data_logic.sessiondata import create_session
from flask import Blueprint, render_template, request, redirect, url_for
import datetime

session_bp = Blueprint('session_routes', __name__)

@session_bp.route('/create_session', methods=['GET', 'POST'])
def create_session_route():
    if request.method == 'GET':
        return render_template('session_creation.html')

    name = request.form['session_name']
    start_date = datetime.datetime.fromisoformat(request.form['start_date'])
    end_date = datetime.datetime.fromisoformat(request.form['end_date'])

    session = create_session(name=name, start_date=start_date, end_date=end_date)

    if session:
        return redirect(url_for('general_routes.index'))

    return render_template('session_creation.html', error=True)