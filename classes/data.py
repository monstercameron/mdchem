from config.config import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(120))
    level_id = db.Column(db.String(120))
    data = db.Column(db.String(120))

    def __init__(self, uid, level_id, data):
        self.uid = uid
        self.level_id = level_id
        self.data = data
