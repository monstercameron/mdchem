from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test

login = Blueprint('login', __name__)

# checks to see if this user has a session cookie


@login.before_request
def require_login():
    # allowed_routes = ['login', 'register', 'index', 'static', 'storage']
    print('endpoint -->', request.endpoint)
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
        pw = request.form['password']
        # query database for user based on the email address submitted in the request
        admin = Admin_test.query.filter_by(email=email).first()
        # checks is the admin exists
        if admin == None:
            return render_template('login.html', title=title, error="email doesn't exists")
        # if the passwords match
        if admin.password == pw:
            title = 'success'
            print('current user data -->', admin.__dict__)
            return render_template('login.html', title=title)
    return render_template('login.html', title=title)
