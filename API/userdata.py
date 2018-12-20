from flask import request, session, Response
from utils.firebase import get_user_data_all, get_user_data
from flask import jsonify
from flask import Blueprint
from classes.token import Token
from classes.admin import Admin_test
from classes.data import Data


userdata = Blueprint('userdata', __name__,)


@userdata.route('userdata', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['POST']

    token = request.headers['Authorization']
    email = request.headers['email']
    user_uuid = request.headers['uuid']

    admin = Admin_test.query.filter_by(email=email).first()
    token_store = Token.query.filter_by(owner_id=admin.id).first()
    user_uuid_data = Data.query.filter_by(uid=user_uuid).all()
    
    
    for data in user_uuid_data:
        print(data.uid ,data.level_id, data.data)

    print(token, token_store.token)

    if token not in token_store.token:
        response = Response(status=401)
        response.data = '{"message":"unauthorized"}'

    elif request.method in allowed_methods:
        data = []
        for userdata in user_uuid_data:
            data.append({'uid': userdata.uid, 'level_id':userdata.level_id, 'data':userdata.data})
        message = {'users':get_user_data(user_uuid), 'data':data}
        response = jsonify(message)

    else:
        response = Response(status=405)
        response.data = '{"message":"method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response