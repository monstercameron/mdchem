from config.config import app
from utils.firebase import get_user_data_all
from flask import jsonify

@app.route('/all', methods=['GET'])
def index():
    users = get_user_data_all()
    return jsonify(users[0].__dict__)
    # return json.dumps(users[0].__dict__)