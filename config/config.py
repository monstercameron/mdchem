from flask import Flask, request, redirect, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://springuser:ThePassword@localhost:3306/db_example'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "TheKeyCanBeAString"

db = SQLAlchemy(app)