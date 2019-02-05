from config.config import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(120))
    target = db.Column(db.String(120))
    message = db.Column(db.TEXT(4294000000))

    def __init__(self, date, target, message):
        self.date = date
        self.target = target
        self.message = message
