from flask import request, session, Response
from datetime import date
from flask import jsonify
from flask import Blueprint
from config.config import db
from classes.token import Token
from classes.admin import Admin_test
from classes.news import News

news = Blueprint('news', __name__,)


@news.route('news', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    if request.method == 'POST':

        # http headers from POST request
        token = request.headers['Authorization']
        email = request.headers['email']

        # database queries to see if admin and corresponding toekn exists
        admin = Admin_test.query.filter_by(email=email).first()
        token_store = Token.query.filter_by(token=token).first()

        # if admin and corresponding token exists then delete all the tokes from the database
        if not admin == None and not token == None:
            token = Token.query.filter_by(owner_id=admin.id).all()
            if len(token) > 0:
                Token.query.filter_by(owner_id=admin.id).delete()
        else:
            response = Response(status=401)
            response.data = '{"message":"unauthorized"}'

    # commit deletions to database
    db.session.commit()    

    else:
            response = Response(status=405)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response