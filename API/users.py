from flask import request
from utils.firebase import get_user_data_all
from flask import jsonify
from flask import Blueprint

users = Blueprint('users', __name__,)


@users.route('users', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():
    allowed_methods = ['POST']

    if request.method in allowed_methods:
        users = get_user_data_all()
        response = jsonify(users)
    else:
        message = {'status': 405, 'message': 'method not allowed'}
        response = jsonify(message)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)
