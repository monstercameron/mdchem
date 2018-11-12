from flask import request, session, Response
from datetime import date
from config.config import db
from classes.news import News
from flask import jsonify
from flask import Blueprint

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

        session['email'] = 'mr.e.cameron@gmail.com'
        print('session -->', session)
        
        if request.headers['Authorization'] not in session['email']:
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

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response