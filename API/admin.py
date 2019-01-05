from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from classes.token import Token
from classes.admin import Admin_test

admins = Blueprint('admins', __name__,)

@admins.route('admin', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    # http header with auth token, quering database if toekn exist
    token = request.headers['Authorization']
    token_obj = Token.query.filter_by(token=token).first()

    # debug message checking to see if the token exists
    print('token exists --> ', not token_obj is None)

    if request.method == 'POST':

        # if toekn is not empty
        if token_obj != None:

            # list to store all admins
            data = []

            # looping through all admins
            for admin in Admin_test.query.all():
                data.append({"name": admin.name, "email": admin.email, "role":admin.role.value})

            # return a json spec list of admins
            response = jsonify(data)

        elif token_obj == None:

            # if the token doesn't exist then user is not authorized
            response = Response(status=401)
            response.data = '{"message":"Not authorized"}'

    else:

        # if HTTP method isn't POST then method not allowed
        response = Response(status=405)
        response.data = '{"message":"Method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
