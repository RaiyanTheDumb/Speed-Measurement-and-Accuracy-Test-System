from flask import Blueprint, render_template
from .text_loader import load_sample_text

main = Blueprint('main', __name__)

@main.route('/')
def index():
    sample_text = load_sample_text()
    return render_template('index.html', sample_text=sample_text)