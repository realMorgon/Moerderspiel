from backend.data_logic.sessiondata import create_session, get_session
from flask import Blueprint, render_template, request, redirect, url_for, session
import datetime

from backend.data_logic.userdata import get_user

session_bp = Blueprint('session_routes', __name__)

@session_bp.route('/create_session', methods=['GET', 'POST'])
def create_session_route():
    if request.method == 'GET':
        return render_template('session_creation.html')

    name = request.form['session_name']
    start_date = datetime.datetime.fromisoformat(request.form['start_date'])
    end_date = datetime.datetime.fromisoformat(request.form['end_date'])

    game_session = create_session(name=name, start_date=start_date, end_date=end_date)

    if game_session:
        return redirect(url_for('general_routes.index'))

    return render_template('session_creation.html', error=True)

@session_bp.route('/join/<session_id>')
def join_session_route(session_id):
    if not 'user_id' in session:
        session['target_session_id'] = session_id
        return redirect(url_for('user_routes.login_route'))
    get_session(session_id).add_user(session['user_id'])
    get_user(session['user_id']).add_session(session_id)
    return redirect(url_for('general_routes.index'))