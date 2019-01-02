from flask import Blueprint, render_template, request, redirect, session, url_for
from classes.admin import Admin_test, Roles
from config.config import db
from utils.validation import validate_email, validate_password
from utils.security import hash_password

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

        print('Register/post')

        # registration form
        first = request.form['first']
        last = request.form['last']
        email = request.form['email']
        email_verify = request.form['email-verify']
        password = request.form['password']
        password_verify = request.form['password-verify']

        # form validation
        if email_verify not in email:
            return render_template('register.html', title=title, first=first, last=last, email=email, error=f"your email wasn't verified correctly, make sure you type in the same email.")

        if password_verify not in password:
            return render_template('register.html', title=title, first=first, last=last, email=email, error=f"your password wasn't verified correctly, make sure you type in the same password.")

        # validate the email format
        if not validate_email(email):
            return render_template('register.html', title=title, first=first, last=last, email=email, error=f"your email: {email} wasn't formatted correctly.")

        # validete the password format
        if not validate_password(password):
            return render_template('register.html', title=title, first=first, last=last, email=email, error="your password wasn't secure enough, must contain atleast 1 uppercase, 1 lowercase and 1 number.")

        # password, recovery hashing
        # hashing the password
        hashed_password = hash_password(password)
        # hashing the recovery question and secret response
        hashed_recovery = hash_password(password)

        # make admin object
        admin = Admin_test(email, first + ' ' + last, hashed_password, hashed_recovery)

        # check if its first user to register
        if len(Admin_test.query.all()) == 0:
            admin.role = Roles.OWNER
        else:
            admin.role = Roles.ADMIN
        # insert into database
        db.session.add(admin)
        db.session.commit()



        # on success
        return redirect(url_for('login.index', success='Successfully registered your account'))

    return render_template('register.html', title=title)
