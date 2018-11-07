from flask import Blueprint, request, redirect, session
from classes.admin import Admin_test

logout = Blueprint('logout', __name__)

# checks to see if this user has a session cookie


@logout.before_request
def require_login():
    print('checking cookie before loggin out -->', request.endpoint)
    print(session)
    if 'email' in session:
        del session['email']

# logout


@logout.route('/logout', methods=['GET', 'POST'])
def index():
    return redirect('/')
