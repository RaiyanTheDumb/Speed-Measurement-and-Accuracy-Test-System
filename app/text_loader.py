import json
import random
import os


def load_sample_text():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'texts', 'samples.json')

    with open(file_path, 'r') as f:
        texts = json.load(f)

    return random.choice(texts)