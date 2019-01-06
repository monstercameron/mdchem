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

    allowed_methods = ['POST', 'GET']

    # request.args.get
    if request.method == 'GET':
        data = []
        for news in News.query.all():
            data.append({'target': news.target, 'date': news.date,
                         'message': news.message})
        response = jsonify(data)
        return response

    elif request.method == 'POST':

        token = request.headers['token']
        email = request.headers['email']
        admin = Admin_test.query.filter_by(email=email).first()
        token_store = Token.query.filter_by(owner_id=admin.id).first()

        if token not in token_store.token:
            response = Response(status=401)
            response.data = '{"message":"unauthorized"}'
        else:
            target = request.headers['target']
            message = request.data
            news = News(date.today(), target, message)
            db.session.add(news)
            db.session.commit()
            response = Response(status=200)
            response.data = '{"message":"saved news"}'

    elif request.method not in allowed_methods:
            response = Response(status=405)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response