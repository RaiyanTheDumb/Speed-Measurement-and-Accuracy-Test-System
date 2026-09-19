"""
config.py
Configuration settings for the Flask application.
Defines file paths and environment settings.
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration class.

    Attributes:
        DEBUG (bool): Enable Flask debug mode.
        TEXTS_PATH (str): Path to sample texts JSON file.
        SCORES_PATH (str): Path to scores CSV file.
    """
    DEBUG = True
    TEXTS_PATH = os.path.join(BASE_DIR, 'data', 'texts', 'samples.json')
    SCORES_PATH = os.path.join(BASE_DIR, 'data', 'scores', 'history.csv')