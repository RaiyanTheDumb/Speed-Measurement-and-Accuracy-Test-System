import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    TEXTS_PATH = os.path.join(BASE_DIR, 'data/texts/samples.json')
    SCORES_PATH = os.path.join(BASE_DIR, 'data/scores/history.csv')