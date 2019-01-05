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
            for user in Data.query.filter_by(level_id=level_id).order_by( desc(Data.score) ).limit(10):

                # append python dictionaries into the list to be jsonified
                data.append({'user': user.owner.email, 'score': user.score})

            # return a json string in the response object to the client         
            response = jsonify(data)

        # if levelid parameter doesn't exist
        else:
            response = Response(status=200)
            response.data = '{"message":"global highscores not yet implemented"}'

    # if not GET methods, status 405 method not allowed with custom error message
    else:
        response = Response(status=405)
        response.data = '{"message":"only supports GET right now"}'

    # cross origin code - not sure what exactly it does, needs research
    response.headers.add('Access-Control-Allow-Origin', '*')

    # return built http response
    return response
