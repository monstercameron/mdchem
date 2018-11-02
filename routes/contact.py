from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test

contact = Blueprint('contact', __name__)

# checks to see if this user has a session cookie


@contact.before_request
def require_login():
    print('require login for endpoint -->', request.endpoint)
    print(session)
    if 'email' in session:
        return redirect('/admin')

# GET - displays the contact form
# POST - submits the contact form


@contact.route('/contact', methods=['GET', 'POST'])
def index():
    title = 'Contact Us!'
    if request.method == 'POST':
        print('POST')
        return render_template('contact.html', title=title, message="Your message was sent!")
    return render_template('contact.html', title=title)
