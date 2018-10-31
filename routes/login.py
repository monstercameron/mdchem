from flask import Blueprint, render_template
import os

templates = os.path.dirname(os.getcwd())+'/mdchem/templates'
static = os.path.dirname(os.getcwd())+'/mdchem/static'

print('static path -->', static)

login = Blueprint('login', __name__,
                  template_folder=templates,  static_folder=static)


@login.route('/login')
def index():
    return render_template('login.html', title="login")
