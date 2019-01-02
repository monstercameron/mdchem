from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
import subprocess

logs = Blueprint('logs', __name__,)

@logs.route('logs', methods=['GET', 'POST', 'DELETE', 'OPTION', 'PUT'])
def index():

    allowed_methods = ['GET']

    # testing
    # request.args.get
    if request.method == 'GET':

        data = []
        line_number = 1

        command = "cp /var/log/apache2/error.log /var/www/mdchem/mdchem/temp/error.log"
        subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        # apache log
        # f = open("/var/log/apache2/error.log", "r")
        f = open("/var/www/mdchem/mdchem/temp/error.log", "r")
        for x in f:
            print(x)
            data.append({"num":line_number, "line":x})
            line_number += 1

        response = jsonify(data)

    return response
