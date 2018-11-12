
from flask import request, session, Response
from utils.firebase import get_user_data_all, user_list
from config.config import db
from classes.data import Data
from flask import jsonify
from flask import Blueprint

save = Blueprint('save', __name__,)


@save.before_request
def auth_list():
    if len(user_list) == 0:
        get_user_data_all()


@save.route('save', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['POST', 'GET']

    # testing
    # request.args.get
    if request.method == 'GET':
        data = []
        for user in Data.query.all():
            # print("test", user.__dict__)
            data.append(
                {'uid': user.uid, 'level_id': user.level_id, 'data': user.data})
        response = jsonify(data)
    elif request.method == 'POST':
        # print('POST request key -->', request.headers['Authorization'])
        # print('the list --> ', '/'.join(user_list))
        if request.headers['Authorization'] not in user_list:
            response = Response(status=401)
            response.data = '{"message":"bad key"}'
        else:
            uid = request.headers['Authorization']
            level = request.headers['level_id']
            body = request.data

            message = {'message': 'data updated'}

            if Data.query.filter_by(uid=uid, level_id=level).first() == None:
                data = Data(uid, level, body)
                db.session.add(data)
                message = {'message': 'data saved'}
            else:
                data = Data.query.filter_by(uid=uid, level_id=level).first()
                data.data = body
            db.session.commit()
            # print(data.__dict__)
            response = jsonify(message)
    else:
        response = Response(status=405)
        response.data = '{"message":"only supports GET and POST right now"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)
