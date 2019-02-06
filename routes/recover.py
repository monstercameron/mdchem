from flask import Blueprint, render_template, request, redirect, session, url_for
from classes.admin import Admin_test
from config.config import db
from utils.security import *
from utils.validation import validate_password
from utils.security import generate_salt, hash_password_with_salt
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

        # error message
        error = "Please Enter A Value!"
        # form data validation
        if not request.form['email']:
            return render_template('recover.html', title=title, error=error, email="is-invalid")
        email = request.form['email']

        if not request.form['security']:
            return render_template('recover.html', title=title, error=error, question="is-invalid")
        question = request.form['security']

        if not request.form['answer']:
            return render_template('recover.html', emailval=email, title=title, error=error, answer="is-invalid")
        answer = request.form['answer']

        # query to see if user exists
        query = Admin_test.query.filter_by(email=email).first()

        # if the user exists then do the following
        if not query is None:

            # makes string of the email, question number and answer
            user_password = email + question + answer

            # compare the old hash against a newly hashed userpassword
            if verify_password(query.recovery, user_password):

                # on success, returns the template that will allows users to reset password
                return render_template('reset.html', title=title, unique=query.unique, security=question, answer=answer)

            else:

                # on fail, prompt the user that the credentials are incorrect
                return render_template('recover.html', title=title, error="Bad Security Question / Password")

        # if the user deson't exist
        else:
            # prompt the user that the email provided doesnt have a user
            error = "User Doesn't exist"
            return render_template('recover.html', title=title, error="User Doesn't Exist", emailval=email)

    # returns template on GET
    return render_template('recover.html', title=title)


@recover.route('/reset', methods=['GET', 'POST'])
def reset():
    title = "Reset Password!"

    if request.method == 'POST':

        # form data validation
        if not request.form['password'] and not request.form['passwordv']:
            return render_template('reset.html', title=title, error="Enter A Password!", password="is-invalid")
        else:
                pw = request.form['password']
                pwv = request.form['passwordv']
                unique = request.form['unique']
                security = request.form['security']
                answer = request.form['answer']

                if pw != pwv:
                        return render_template('reset.html', title=title, error="Passwords Don't Match", password="is-invalid")
                elif not validate_password(pw):
                        return render_template('reset.html', title=title, error="Password Is Not Valid", password="is-invalid")
                else:
                        salt = generate_salt()
                        admin = Admin_test.query.filter_by(unique=unique).first()
                        admin.password = hash_password_with_salt(pw, salt)
                        recovery = admin.email+security+answer
                        admin.recover = hash_password_with_salt(recovery, salt)
                        db.session.commit()
                        return redirect(url_for('login.index'))

    # display reset form
    return redirect(url_for('recover.index')) 
