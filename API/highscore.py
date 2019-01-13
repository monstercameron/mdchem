from flask import request, Response, jsonify, Blueprint
from sqlalchemy import desc
from config.config import db
from classes.data import Data
from classes.student import Student

highscore = Blueprint('highscore', __name__,)


@highscore.route('highscore', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    # http GET method, no authorization
    if request.method == 'GET':

        # GET parameter, levelid for highscore
        level_id = request.args.get('levelid')

        # list to store all request data - probably inefficient
        data = []

        # checks to see if the levelid parameter exists
        if not level_id is None:

            # retrieve all score entries and loop thought the returned list
            # query return the data ojects with the highest scores
            for student in Data.query.filter_by(level_id=level_id).order_by(desc(Data.score)).limit(10):

                # append python dictionaries into the list to be jsonified
                data.append({'user': student.owner.email,
                             'score': student.score})

            # return a json string in the response object to the client
            response = jsonify(data)

        # if levelid parameter doesn't exist
        else:

            # getting all students

            for student in Student.query.order_by(desc(Student.score)).limit(10):

                # append python dictionaries into the list to be jsonified
                data.append({'user': student.email, 'score': student.score})

            # return a json string in the response object to the client
            response = jsonify(data)

    # if not GET methods, status 405 method not allowed with custom error message
    else:
        response = Response(status=405)
        response.data = '{"message":"only supports GET right now"}'

    # cross origin code - not sure what exactly it does, needs research
    response.headers.add('Access-Control-Allow-Origin', '*')

    # return built http response
    return response


@highscore.route('highscorebuildindex', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def build():

    rebuild_highscore_task()

    # # gettin all students
    # students = Student.query.all()

    # for student in students:

    #     # var to hold the score per student
    #     score = 0

    #     # get all data objects belonging to the student
    #     for data in Data.query.filter_by(owner=student).all():

    #         # add all the scores together, note 1 data object per level
    #         score += data.score

    #     student.score = score

    #     # debud print statement
    #     print('student-->', student.email, ' | score-->', score)

    # # saving students back to data base
    # db.session.commit()

    response = Response(status=200)
    response.data = '{"message":"rebuilt highscore index"}'

    # return built http response
    return response


def rebuild_highscore_task():
    print('Rebuilding Highscores!')

     # gettin all students
    students = Student.query.all()

    for student in students:

        # var to hold the score per student
        score = 0

        # get all data objects belonging to the student
        for data in Data.query.filter_by(owner=student).all():

            # add all the scores together, note 1 data object per level
            score += data.score

        student.score = score

        # debug print statement
        # print('student-->', student.email, ' | score-->', score)

    # saving students back to data base
    db.session.commit()
