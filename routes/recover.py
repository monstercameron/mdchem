from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test

recover = Blueprint('recover', __name__)

# checks to see if this user has a session cookie


@recover.before_request
def require_login():
    print('require login for endpoint -->', request.endpoint)
    print(session)
    if 'email' in session:
        return redirect('/admin')

# GET - displays the recover form
# POST - submits the recover form


@recover.route('/recover', methods=['GET', 'POST'])
def index():
    title = 'login'
    if request.method == 'POST':
        print('POST')
    return render_template('recover.html', title=title)
