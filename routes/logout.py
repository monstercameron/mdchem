from flask import Blueprint, request, redirect, session
from classes.admin import Admin_test
from classes.token import Token
from config.config import db

logout = Blueprint('logout', __name__)

# checks to see if this user has a session cookie


@logout.before_request
def require_login():
    print('checking cookie before loggin out -->', request.endpoint)
    print(session)
#     if 'email' in session:
#         del session['email']

# logout


@logout.route('/logout', methods=['GET', 'POST'])
def index():
    admin = Admin_test.query.filter_by(email=session['email']).first()

    if not admin == None:
        token = Token.query.filter_by(owner_id=admin.id).all()
        if len(token) > 0:
            Token.query.filter_by(owner_id=admin.id).delete()

    db.session.commit()    
    del session['email']
    return redirect('/')
