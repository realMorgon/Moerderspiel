import bcrypt
from flask import Blueprint, render_template, request, session, redirect, url_for
from backend.data_logic.userdata import create_user, get_user_by_name

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/create_user', methods=['GET','POST'])
def create_user_route():
    if request.method == 'GET':
        return render_template('user_creation.html')
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        raise "Passwords do not match"

    user = create_user(name=name, password=password, email=email, force=False)
    session['user_id'] = user.id
    if user:
        return redirect(url_for('general_routes.index'))

    return render_template('user_creation.html')

@user_bp.route('/login', methods=['GET','POST'])
def login_route():
    if request.method == 'GET':
        return render_template('login.html')
    name = request.form['name']
    password = request.form['password']
    user = get_user_by_name(name)
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        session['user_id'] = user.id
        return redirect(url_for('general_routes.index'))

    return None