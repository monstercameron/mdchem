from flask import request, session, Response
from utils.firebase import get_user_data_all
from flask import jsonify
from flask import Blueprint

users = Blueprint('users', __name__,)


@users.route('users', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['POST']

    session['email'] = 'mr.e.cameron@gmail.com'
    print('session -->', session)

    if request.headers['Authorization'] not in session['email']:
        message = {'status': 401, 'message': 'unauthorized'}
        response = jsonify(message)

    elif request.method in allowed_methods:
        users = get_user_data_all()
        message = {'status':200, 'users':users}
        response = jsonify(users)

    else:
        message = {'status': 405, 'message': 'method not allowed'}
        response = jsonify(message)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)