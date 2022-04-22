from App.database import db
from .user import User #???

class MyScore(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    score = db.Column('score', db.Integer, nullable=True)
