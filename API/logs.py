from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from shutil import copyfile

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
        # copyfile("/var/www/mdchem/mdchem/nohup.out","/var/www/mdchem/mdchem/nohup.out.bk")
        # f = open("/var/www/mdchem/mdchem/nohup.out.bk","r").read().split('\n')
    
        for x in f:
           print(x)
           if x == "":
               f.remove(x)

           data.append({"num":line_number, "line":x})
           line_number += 1

        # for str in f:
           # if str == "":
               # f.remove(str)

        response = jsonify(data)

    return response
