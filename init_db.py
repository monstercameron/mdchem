from config.config import db
from classes.admin import Admin_test
from classes.data import Data
from classes.student import Student
from classes.news import News
from classes.token import Token

db.drop_all()
db.create_all()