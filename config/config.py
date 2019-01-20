from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import logging
from logging.handlers import RotatingFileHandler



local = True

if local:
    static = os.getcwd()+'/static'
    templates = os.getcwd()+'/templates'
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


formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('logs/log.txt', maxBytes=10000000, backupCount=5)
handler.setLevel(logging.NOTSET)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

from services.services import make_service
# making services
service = make_service(app)
