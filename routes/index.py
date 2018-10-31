from flask import Blueprint

simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/')
def show():
    return "index \n <a href='/api/all-users'> all users </a>"
