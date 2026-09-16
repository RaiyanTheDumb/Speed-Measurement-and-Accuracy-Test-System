from flask import Blueprint, render_template, request, jsonify
from .text_loader import load_sample_text
from .calculator import (calculate_wpm, calculate_accuracy, calculate_errors, get_typing_level)
from .score_logger import (save_score_csv, save_score_json, get_high_score, get_all_scores)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    sample_text = load_sample_text()
    high_score = get_high_score()
    return render_template('index.html',
                           sample_text=sample_text,
                           high_score=high_score)


@main.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    typed_text = data.get('typed_text', '')
    sample_text = data.get('sample_text', '')
    time_seconds = data.get('time_seconds', 0)

    wpm = calculate_wpm(typed_text, time_seconds)
    accuracy = calculate_accuracy(sample_text, typed_text)
    errors = calculate_errors(sample_text, typed_text)
    level = get_typing_level(wpm)

    save_score_csv(wpm, accuracy, errors, time_seconds, level)
    save_score_json(wpm, accuracy, errors, time_seconds, level)

    return jsonify({
        'wpm': wpm,
        'accuracy': accuracy,
        'errors': errors,
        'level': level
    })

@main.route('/history')
def history():
    scores = get_all_scores()
    high_score = get_high_score()
    return render_template('history.html',
                           scores=scores,
                           high_score=high_score)