from flask import Blueprint, render_template, jsonify, request, send_from_directory
from App.controllers import words
from App.database import db
from App.models import Words

wordlist_views = Blueprint('wordlist_views', __name__, template_folder='../templates')

@wordlist_views.route('/wordlist', methods=['GET'])
def list_words():
    word_list = Words.query.all()
    return render_template('wordList.html', word_list = word_list)