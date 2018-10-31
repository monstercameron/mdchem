from flask import Blueprint

login = Blueprint('login', __name__, template_folder='templates')


@login.route('/login')
def index():
    return "login \n <a href='/'> index </a>"
