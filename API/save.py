from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from utils.firebase import get_user_data_all
from config.config import db
from classes.data import Data
from classes.student import Student
from utils.firebase import new_user_to_database

save = Blueprint('save', __name__,)


# @save.before_request
# def auth_list():
#     new_user_to_database()


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
                {'level_id': user.level_id,
                 'data': user.data,
                 'score': user.score})
        response = jsonify(data)
    elif request.method == 'POST':

        uid = request.headers['uuid']
        level = request.headers['level_id']
        body = request.data

        if Student.query.filter_by(uid=uid).all():


            if Data.query.filter_by(level_id=level, owner=Student.query.filter_by(uid=uid).first()).first() == None:
                data = Data(level, body, 25,
                            Student.query.filter_by(uid=uid).first())
                db.session.add(data)
                message = {'message': 'data saved'}
            else:
                data = Data.query.filter_by(
                    level_id=level, owner=Student.query.filter_by(uid=uid).first()).first()
                print('this is the data --> ', data.__dict__)
                data.data = body
                message = {'message': 'data updated'}

            db.session.commit()
            # print(data.__dict__)
            response = jsonify(message)

        elif not Student.query.filter_by(uid).all():
            response = Response(status=401)
            response.data = '{"message":"bad uuid"}'

    else:
        response = Response(status=405)
        response.data = '{"message":"only supports GET and POST right now"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
