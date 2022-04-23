from flask import Blueprint, render_template, jsonify, request, send_from_directory
from App.controllers import words

play_views = Blueprint('play_views', __name__, template_folder='../templates')

word_list = []
@play_views.route('/play', methods=['GET'])
def play_game():
    return render_template('play.html')