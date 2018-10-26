from config.config import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
