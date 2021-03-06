from flask import request, session, Response
from utils.firebase import get_user_data_all, get_user_data
from flask import jsonify
from flask import Blueprint
from classes.token import Token
from classes.admin import Admin_test
from classes.data import Data
from classes.student import Student


userdata = Blueprint('userdata', __name__,)


@userdata.route('userdata', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    # http headers
    token = request.headers['token']
    uuid = request.headers['uuid']

    # getting admin via back reference in token object
    admin = Token.query.filter_by(token=token).first()

    # getting student via uuid
    student = Student.query.filter_by(uid=uuid).first()


    if request.method == 'POST':
        if not admin is None and not student is None:

            # getting all data objects owned by specified student
            student_data = Data.query.filter_by(owner=student).all()

            data = []
            
            data.append({'email': student.email, 'uuid':student.uid})

            print(student_data)

            for userdata in student_data:
                data.append({'level_id': userdata.level_id,
                 'data': userdata.data,
                 'score': userdata.score})
            
            
            # message = {'users': get_user_data(user_uuid), 'data': data}
            response = jsonify(data)

        elif student is None:
            response = Response(status=400)
            response.data = '{"message":"bad student uuid"}'
        else:
            response = Response(status=401)
            response.data = '{"message":"user not authorized"}'

    else:
        response = Response(status=405)
        response.data = '{"message":"method not allowed"}'

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@userdata.route('completion', methods=['GET'])
def completion():

    complete = 0
    completed = False
    incomplete = 0
    student_data = []

    # get a list of all student objects
    allStudents = Student.query.all()

    for student in allStudents:

        # get a list of all level objects related to the user
        student_data = Data.query.filter_by(owner=student).all()

        # iterate through the list and if the list has a level object with id of 9 increment complete
        for data in student_data:
            if data.level_id == '9':
                complete += 1
                completed = True

        # check if user has completed flag, else increment incomplete
        if not completed:
            incomplete += 1
        
        # reset completed flag
        completed = False

    response = Response(status=200)
    response.data = f'{{"complete":{complete},"incomplete":{incomplete}}}'
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response