from config.config import app
from utils.firebase import get_user_data_all
import json
from flask import jsonify
# import routes.index as index


@app.route('/', methods=['GET'])
def index():
    users = get_user_data_all()
    return jsonify(users[0].__dict__)
    # return json.dumps(users[0].__dict__)

if __name__ == '__main__':
    app.run()
