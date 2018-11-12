from config.config import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(120))
    message = db.Column(db.String(255))

    def __init__(self, date, damessageta):
        self.date = date
        self.message = message
