from flask import request, session, Response
from flask import jsonify
from flask import Blueprint
from config.config import db
from classes.token import Token
from utils.validation import validate_email, validate_password
from utils.security import hash_password, verify_password

update = Blueprint('update', __name__,)


@update.route('update', methods=['POST'])
def index():

    if request.method == 'POST':

         # update form
        secret = request.headers['token']
        oldpassword = request.headers['oldpassword']
        password = request.headers['password']
        pwverify = request.headers['pwverify']

        token = Token.query.filter_by(token=secret).first()

        if token != None:

            # form validation
            if pwverify not in password:
                response = Response(status=400)
                response.data = '''{"message":"password doesn't match"}'''

            # validate the password format
            elif not validate_password(password):
                response = Response(status=400)
                response.data = '''{"message":"password isn't properly formatted"}'''

            # validates old password
            elif not verify_password(token.owner.password, oldpassword):
                response = Response(status=400)
                response.data = '''{"message":"There is something wrong with the current password"}'''

            else:
                token.owner.password = hash_password(password)
                db.session.commit()
                response = Response(status=200)
                response.data = '''{"message":"admin password updated"}'''

            return response
        else:
            response = Response(status=401)
            response.data = '{"message":"user is not authorized to make account level change"}'
            return response

    else:
        response = Response(status=405)
        response.data = '{"message":"endpoint ony allows POST method"}'
        return response
