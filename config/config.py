from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import logging
from logging.handlers import RotatingFileHandler
from credentials import *

# get file directories
static = os.getcwd()+'/static'
templates = os.getcwd()+'/templates'

# confifure flask core
app = Flask(__name__, static_folder=static, template_folder=templates)
app.config['SQLALCHEMY_DATABASE_URI'] = mysql
app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = secret_key

#  setup flask cors for cross domain api calls
CORS(app, resources=r'/api/*')

# init mysql orm module
db = SQLAlchemy(app)

# formatter = logging.Formatter(
#         "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
# handler = RotatingFileHandler('logs/log.txt', maxBytes=10000000, backupCount=5)
# handler.setLevel(logging.NOTSET)
# handler.setFormatter(formatter)
# app.logger.addHandler(handler)

# from services.services import make_service
# from services.services import make_service
# making services
# service = make_service(app)
