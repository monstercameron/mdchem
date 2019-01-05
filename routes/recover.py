from flask import Blueprint, render_template, request, redirect, session
from classes.admin import Admin_test
from config.config import db
from utils.security import *

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

        # form data
        email = request.form['email']
        question = request.form['question']
        answer = request.form['answer']

        # query to see if user exists
        query = Admin_test.query.filter_by(email=email).first()

        # if the user exists then do the following
        if not query is None:
            
            # makes string of the email, question number and answer
            user_password =email + question + answer

            # compare the old hash against a newly hashed userpassword
            if verify_password(query.recovery, user_password):

                # returns the template that will allows users to reset password
                return render_template('recover.html', title=title)

        # if the user deson't exist
        else:
            # prompt the user that the email provided doesnt have a user
            error = "User Doesn't exist"
            return render_template('recover.html', title=title, error=error)

    # returns template on GET
    return render_template('recover.html', title=title)