from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from classes.token import Token
from classes.admin import Admin_test
from utils.firebase import new_user_to_database
from classes.student import Student


users = Blueprint('users', __name__,)


@users.route('users', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    token = request.headers['token']
    token_local = Token.query.filter_by(token=token).first()
    print('Token exists --> ', not token_local is None)

    if request.method == 'POST':
        if token_local is None:
            response = Response(status=401)
            response.data = '{"message":"unauthorized"}'

        else:
            new_user_to_database()
            users = []
            for student in Student.query.all():
                users.append({'email': student.email, 'UID': student.uid})
            response = jsonify(users)

    else:
        response = Response(status=405)
        response.data = '{"message":"method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)
