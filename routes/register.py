from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test

register = Blueprint('register', __name__)

# checks to see if this user has a session cookie


@register.before_request
def require_login():
    # allowed_routes = ['login', 'register', 'index', 'static', 'storage']
    print('require login for endpoint -->', request.endpoint)
    print(session)
    if 'email' in session:
        return redirect('/admin')

# GET - displays the register form
# POST - submits the register form


@register.route('/register', methods=['GET', 'POST'])
def index():
    title = 'login'
    if request.method == 'POST':
        print('POST')
    return render_template('register.html', title=title)
