from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test

admin = Blueprint('admin', __name__)

# checks to see if this user has a session cookie


@admin.before_request
def require_login():
    # allowed_routes = ['login', 'register', 'index', 'static', 'storage']
    print('require login for endpoint -->', request.endpoint)
    print(session)
    if 'email' in session:
        return redirect('/admin')

# GET - displays the login form
# POST - submits the login form


@admin.route('/login', methods=['GET', 'POST'])
def index():
    title = 'login'
    if request.method == 'POST':
        print('Admin - post')
    return render_template('login.html', title=title)
