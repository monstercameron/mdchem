from flask import request, session, Response
from utils.firebase import get_user_data_all
from flask import jsonify
from flask import Blueprint
from classes.token import Token
from classes.admin import Admin_test


users = Blueprint('users', __name__,)


@users.route('users', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['POST']

    token = request.headers['Authorization']
    email = request.headers['email']
    admin = Admin_test.query.filter_by(email=email).first()
    token_store = Token.query.filter_by(owner_id=admin.id).first()

    print(token, token_store.token)

    if token not in token_store.token:
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