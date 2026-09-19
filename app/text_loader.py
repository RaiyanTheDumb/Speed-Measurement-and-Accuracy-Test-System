"""
text_loader.py
Loads and returns a random sample text for the typing test.
"""
import json
import random
import os


def load_sample_text():
    """
    Load a random sample text from the JSON data file.

    Reads all texts from data/texts/samples.json
    and returns one at random for each test session.

    Returns:
        str: A randomly selected sample text string.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'texts', 'samples.json')

    with open(file_path, 'r') as f:
        texts = json.load(f)

    return random.choice(texts)