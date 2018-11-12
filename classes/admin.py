from config.config import db
from classes.token import Token


class Admin_test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    password = db.Column(db.String(255))
    recovery = db.Column(db.String(255))
    token = db.relationship('Token', backref='owner')

    def __init__(self, email, name, password, recovery):
        self.email = email
        self.name = name
        self.password = password
        self.recovery = recovery
