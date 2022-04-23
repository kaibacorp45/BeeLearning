from App.database import db #change to word model with difficulty as columns

class Words(db.Model):
    wid = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable = False)
    difficulty = db.Column(db.String(50), nullable = True)
    partOfSpeech = db.Column(db.String(50), nullable = True)
    defintion = db.Column(db.String(500), nullable = True)
    sentence = db.Column(db.String(500), nullable = True)

    def toDict(self):
        return{
            'wid': self.wid,
            'word': self.username,
            'difficulty': self.difficulty,
            'partOfSpeech': self.partOfSpeech,
            'definition': self.defintion,
            'sentence': self.sentence
        }