from config.config import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.String(120))
    score = db.Column(db.Integer)
    data = db.Column(db.TEXT)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, level_id, data, score, owner):
        self.level_id = level_id
        self.data = data
        self.score = score
        self.owner = owner
