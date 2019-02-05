from flask import request, session, Response
from utils.firebase import get_user_data_all, get_user_data
from flask import jsonify
from flask import Blueprint
from utils.firebase import new_user_to_database

updatestudent = Blueprint('updatestudent', __name__,)

@updatestudent.route('updatestudent', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    if request.method == 'GET':
        print('Updating Students...')
        new_user_to_database()
        response = Response(status=200)
        response.data = '{"message":"Student Database Updated!"}'
    else:
        response = Response(status=405)
        response.data = '{"message":"method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response