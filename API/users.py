from flask import request, session, Response
from utils.firebase import get_user_data_all
from flask import jsonify
from flask import Blueprint
from config.config import tokens

users = Blueprint('users', __name__,)


@users.route('users', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['POST']

    session['email'] = 'mr.e.cameron@gmail.com'
    print('session -->', session)
    print('tokens -->', tokens[session['email']])

    if request.headers['Authorization'] not in tokens[session['email']]:
        response = Response(status=401)
        response.data = '{"message":"unauthorized"}'

    elif request.method in allowed_methods:
        users = get_user_data_all()
        message = {'users':users}
        response = jsonify(users)

    else:
        response = Response(status=405)
        response.data = '{"message":"method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)