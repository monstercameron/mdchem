from flask import request, session, Response
from flask import jsonify
from flask import Blueprint

logs = Blueprint('logs', __name__,)

@logs.route('logs', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['GET']

    # testing
    # request.args.get
    if request.method == 'GET':

        data = []
        line_number = 1

        # apache log
        # f = open("/var/log/apache2/error.log", "r")
        f = open("/home/monstercameron/Desktop/python/mdchem/logs/log.txt", "r")
        for x in f:
            print(x)
            data.append({"num":line_number, "line":x})
            line_number += 1

        response = jsonify(data)

    return response
