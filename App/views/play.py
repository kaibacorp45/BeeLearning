from flask import Blueprint, render_template, jsonify, request, send_from_directory

play_views = Blueprint('play_views', __name__, template_folder='../templates')

@play_views.route('/play', methods=['GET'])
def play_game():
    return render_template('play.html')