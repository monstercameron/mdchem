from config.config import db


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey('admin_test.id'))

    def __init__(self, token, owner):
        self.token = token
        self.owner = owner
