from config.config import db
from classes.token import Token
import enum
from sqlalchemy import Enum
import uuid


class Roles(enum.Enum):
    OWNER = 1
    ADMIN = 2
    USER = 3


class Admin_test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    password = db.Column(db.String(255))
    recovery = db.Column(db.String(255))
    unique = db.Column(db.String(255))
    role = db.Column(Enum(Roles))
    token = db.relationship('Token', backref='owner')

    def __init__(self, email, name, password, recovery):
        self.email = email
        self.name = name
        self.password = password
        self.recovery = recovery
        self.unique = uuid.uuid4().hex
