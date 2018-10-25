from flask import Flask, request, redirect, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime, os
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://springuser:ThePassword@localhost:3306/db_example'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "TheKeyCanBeAString"
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()
