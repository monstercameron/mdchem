from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from classes.token import Token
from classes.admin import Admin_test

admins = Blueprint('admins', __name__,)


@admins.route('admin', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    token = request.headers['Authorization']
    token_obj = Token.query.filter_by(token=token).first()

    # checking to see if the token exists
    print('token exists --> ', not token_obj is None)

    if request.method == 'POST':
        if token_obj != None:

            data = []
            for admin in Admin_test.query.all():
                data.append({"name": admin.name, "email": admin.email, "role":admin.role.value})

            response = jsonify(data)

        elif token_obj == None:

            response = Response(status=401)
            response.data = '{"message":"Not authorized"}'

    else:

        response = Response(status=405)
        response.data = '{"message":"Method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)
