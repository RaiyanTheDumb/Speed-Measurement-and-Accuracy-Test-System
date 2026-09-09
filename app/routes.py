from flask import Blueprint, render_template, request, jsonify
from .text_loader import load_sample_text
from .calculator import calculate_wpm, calculate_accuracy, calculate_errors

main = Blueprint('main', __name__)

@main.route('/')
def index():
    sample_text = load_sample_text()
    return render_template('index.html', sample_text=sample_text)


@main.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    typed_text = data.get('typed_text', '')
    sample_text = data.get('sample_text', '')
    time_seconds = data.get('time_seconds', 0)

    wpm = calculate_wpm(typed_text, time_seconds)
    accuracy = calculate_accuracy(sample_text, typed_text)
    errors = calculate_errors(sample_text, typed_text)

    return jsonify({
        'wpm': wpm,
        'accuracy': accuracy,
        'errors': errors
    })