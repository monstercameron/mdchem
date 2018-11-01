from flask import Blueprint, render_template, request
from classes.admin import Admin_test
import os

templates = os.path.dirname(os.getcwd())+'/mdchem/templates'
static = os.path.dirname(os.getcwd())+'/mdchem/static'

print('static path -->', static)

login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def index():
    title = 'login'
    if request.method == 'POST':
        print('email -->', request.form['email'],
              ',password -->',  request.form['password'])
        # save email and password into variables from the request
        email = request.form['email']
        pw = request.form['password']
        # query database for user based on the email address submitted in the request
        admin = Admin_test.query.filter_by(email=email).first()
        # if the passwords match
        if admin.password == pw:
            title = 'success'
            print('current user data -->', admin.__dict__)
            return render_template('login.html', title=title)
    return render_template('login.html', title=title)
