from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


local = False

if local:
    static = os.path.dirname(os.getcwd())+'/mdchem/static'
    templates = os.path.dirname(os.getcwd())+'/mdchem/templates'
    app = Flask(__name__, static_folder=static, template_folder=templates)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://springuser:ThePassword@localhost:3306/db_example'
else:
    static = '/var/www/mdchem/mdchem/static'
    templates = '/var/www/mdchem/mdchem/templates'
    app = Flask(__name__, static_folder=static, template_folder=templates)
    app.config['DEBUG'] = True
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:mdchem123!@localhost:3306/mdchem'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "TheKeyCanBeAString"
CORS(app, resources=r'/api/*')
db = SQLAlchemy(app)
