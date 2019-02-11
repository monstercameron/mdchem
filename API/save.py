from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from utils.firebase import get_user_data_all
from config.config import db
from classes.data import Data
from classes.student import Student
from utils.firebase import new_user_to_database

save = Blueprint('save', __name__,)

@save.route('save', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    # testing
    # request.args.get
    # http GET method, no authorization
    if request.method == 'GET':

        # list to store all request data - probably inefficient
        data = []
        
        # retrieve all score entries and loop thought the returned list
        for user in Data.query.all():
            # append python dictionaries into the list to be jsonified
            data.append({'level_id': user.level_id,'data': user.data,'score': user.score})

        # return a json string in the response object to the client         
        response = jsonify(data)
    
    # http POST method, needs authorization
    elif request.method == 'POST':

        # uuid is used as the auth factor to save data to the server
        # probably an insecure method
        uid = request.headers['uuid']
        level = request.headers['levelid']
        score = request.headers['score']
        body = request.data

        student = Student.query.filter_by(uid=uid).first()

        # if the queryied list of students isn't empty
        if student != None:

            # if the student had data objects saved already with level id
            if Data.query.filter_by(level_id=level, owner=student).first() == None:
                
                # creating new data object
                data = Data(level, body, score, student)

                #  print('with levelid------->',data.__dict__)

                # saving to database
                db.session.add(data)
                message = {'message': 'data saved'}

            # if the student didn't have data objects saved already with level id
            else:

                # retrieving data object
                data = Data.query.filter_by(level_id=level, owner=student).first()
                
                # update the data object and and save to database
                data.data = body

                # update the data object score field
                data.score = score
                
                # debug output    
                # print('Without levelid-------> ', data.__dict__)

                # custom response message
                message = {'message': 'data updated'}

            # committing saves and updates to database
            db.session.commit()
            # print(data.__dict__)
            response = jsonify(message)

        # if no students were found with the given uuid
        elif not Student.query.filter_by(uid=uid).all():
            # status 401 unauthorized with custom error message
            response = Response(status=401)
            response.data = '{"message":"bad uuid"}'

    # if not POST or GET methods, status 405 method not allowed with custom error message
    else:
        response = Response(status=405)
        response.data = '{"message":"only supports GET and POST right now"}'

    # cross origin code - not sure what exactly it does, needs research
    response.headers.add('Access-Control-Allow-Origin', '*')

    # return built http response
    return response
