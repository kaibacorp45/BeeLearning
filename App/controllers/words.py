from App.models import Words
from App.database import db #new
import csv #new

#function to add words
def addWords():
    word_list = []
    with open('/workspace/flaskmvc/WordsList.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            word_list.append(Words(word = line['Word']), difficulty = line['Difficulty'], partOfSpeech = line['POS'], 
            definition = line['Definition'], sentence = ['Sentence'])

    for w in word_list:
        db.session.add(w)
        print(w.word)
    db.session.commit()

def get_all_words():
    return User.query.all()
