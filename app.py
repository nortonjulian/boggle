from flask import Flask, request, jsonify, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    # high_score = session.get('high_score', 0)
    # num_of_plays = session.get('num_of_plays', 0)

    # return render_template('board.html', board=board, high_score=high_score, num_of_plays=num_of_plays)

@app.route('/check-word')
def check_word():
    word = request.args.get('word')
    board = session['board']
    is_valid = boggle_game.check_valid_word(word, board)
    return jsonify({'response': is_valid})

@app.route('/post-score', methods=['POST'])
def post_score():
    """Receive score, update num_of_plays, update high_score if"""

    score = request.json['score']
    high_score = session.get('high_score', 0)
    num_of_plays = session.get('num_of_plays', 0)

    session['num_of_plays'] = num_of_plays + 1
    session['high_score'] = max(score, high_score)

    return jsonify(brokeRecord=score > high_score)
