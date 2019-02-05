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
        target = request.args.get('target')

        if request.args.get('target'):
            print('filtered!!!!!!!!!!!!!!1',target)
            data = []
            for news in News.query.filter_by(target=target):
                data.append({'target': news.target, 'date': news.date,
                            'message': news.message})
            response = jsonify(data)
            return response
        else:
            print('Not filtered!!!!!!!!!!!!!!1')
            data = []
            for news in News.query.all():
                data.append({'target': news.target, 'date': news.date,
                            'message': news.message})
            response = jsonify(data)
            return response
    elif request.method == 'POST':

        token = request.headers['key']
        print('this is the key -->', token)

        token_store = Token.query.filter_by(token=token).first()

        if token_store is None:
            print('this is the token -->', token_store)
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
