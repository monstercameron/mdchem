from config.config import db
from classes.data import Data


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(120))
    email = db.Column(db.String(120))
    score = db.Column(db.Integer)
    data = db.relationship('classes.data.Data', backref='owner')

    def __init__(self, uid, email):
        self.uid = uid
        self.email = email
