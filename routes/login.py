from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test
from utils.validation import validate_email, validate_password
from utils.security import verify_password
from classes.token import Token
from classes.admin import Admin_test
from config.config import db
import uuid

login = Blueprint('login', __name__)

# checks to see if this user has a session cookie


@login.before_request
def require_login():
    # allowed_routes = ['login', 'register', 'index', 'static', 'storage']
    print('require login for endpoint -->', request.endpoint)
    print(session)
    if 'email' in session:
        return redirect('/admin')

# GET - displays the login form
# POST - submits the login form


@login.route('/login', methods=['GET', 'POST'])
def index():
    title = 'login'
    if request.method == 'POST':
        print('email -->', request.form['email'],
              ',password -->',  request.form['password'])
        # save email and password into variables from the request
        email = request.form['email']
        password = request.form['password']
        # validate email
        if not validate_email(email):
            return render_template('login.html', title=title, error="Email isn't porperly formatted")
        # query database for user based on the email address submitted in the request
        admin = Admin_test.query.filter_by(email=email).first()
        # checks is the admin exists
        if admin == None:
            return render_template('login.html', title=title, error="Email doesn't exists")
        # validate password
        if not validate_password(password):
            return render_template('login.html', title=title, error="Password error")
        # if the passwords match sucessful login
        print('password verification -->',
              verify_password(admin.password, password))
        if verify_password(admin.password, password):
            # adding email to session
            session['email'] = email
            token = uuid.uuid4().hex
            token_store = Token(token, admin)
            db.session.add(token_store)
            db.session.commit()
            print('current admin data -->', admin.__dict__)
            return redirect('/admin')
        else:
            return render_template('login.html', title=title, error="Bad Password")
    return render_template('login.html', title=title)
