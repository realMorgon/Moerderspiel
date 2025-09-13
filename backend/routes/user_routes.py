from flask import Blueprint, render_template, request
from backend.data_logic.userdata import create_user

bp = Blueprint('user_routes', __name__)

@bp.route('/create_user', methods=['GET','POST'])
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
    return render_template('user_creation.html', user=user)