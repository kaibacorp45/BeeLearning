from App.models import Words
from App.database import db #new

#function to add words
def addWords():
    word_list = []
    with open('/workspace/flaskmvc/WordsList.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            word_list.append(Words(word = line['Word']), difficulty = line['Difficulty'], partOfSpeech = line['POS'], 
            definition = line['Definition'], sentence = ['Sentence'])
            #print("hi")

    for w in word_list:
        db.session.add(w)
    db.session.commit()

