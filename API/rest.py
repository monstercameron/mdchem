from utils.firebase import get_user_data_all
from flask import jsonify
# import json
from flask import Blueprint

all_users = Blueprint('all_users', __name__, template_folder='templates')


@all_users.route('/api/all-users', methods=['GET'])
def index():
    users = get_user_data_all()
    response = jsonify(users)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return json.dumps(users)
