"""
score_logger.py
Handles saving and retrieving typing test scores
using CSV and JSON local storage.
"""
import csv
import json
import os
from datetime import datetime

SCORES_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', 'data', 'scores', 'history.csv')

SCORES_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '..', 'data', 'scores', 'history.json')


def save_score_csv(wpm, accuracy, errors, time_taken, level):
    """
    Save a test result to the CSV history file.

    Appends a new row with date, time, WPM, accuracy,
    errors and level. Creates the file with headers
    if it does not already exist.

    Args:
        wpm (int): Words per minute score.
        accuracy (int): Accuracy percentage.
        errors (int): Number of errors made.
        time_taken (int): Time taken in seconds.
        level (str): Typing level label.
    """
    file_exists = os.path.exists(SCORES_CSV) and \
                  os.path.getsize(SCORES_CSV) > 0

    with open(SCORES_CSV, 'a', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

        if not file_exists:
            writer.writerow(['date', 'time_taken', 'wpm',
                             'accuracy', 'errors', 'level'])

        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            time_taken,
            wpm,
            accuracy,
            errors,
            level
        ])


def save_score_json(wpm, accuracy, errors, time_taken, level):
    """
    Save a test result to the JSON history file.

    Loads existing scores, appends the new entry,
    and writes back to the JSON file.

    Args:
        wpm (int): Words per minute score.
        accuracy (int): Accuracy percentage.
        errors (int): Number of errors made.
        time_taken (int): Time taken in seconds.
        level (str): Typing level label.
    """
    new_entry = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'time_taken': time_taken,
        'wpm': wpm,
        'accuracy': accuracy,
        'errors': errors,
        'level': level
    }

    if os.path.exists(SCORES_JSON):
        with open(SCORES_JSON, 'r') as f:
            data = json.load(f)
    else:
        data = []

    data.append(new_entry)

    with open(SCORES_JSON, 'w') as f:
        json.dump(data, f, indent=4)


def get_high_score():
    """
    Retrieve the highest WPM score ever recorded.

    Reads all rows from the CSV history file
    and returns the maximum WPM value found.

    Returns:
        int: Highest WPM score. Returns 0 if no scores exist.
    """
    if not os.path.exists(SCORES_CSV):
        return 0

    high = 0
    with open(SCORES_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                if int(row['wpm']) > high:
                    high = int(row['wpm'])
            except (ValueError, KeyError):
                pass

    return high


def get_all_scores():
    """
    Retrieve all test scores from the CSV history file.

    Returns:
        list: List of dicts representing each score row.
              Returns empty list if no scores file exists.
    """
    if not os.path.exists(SCORES_CSV):
        return []

    scores = []
    with open(SCORES_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores.append(row)

    return scores