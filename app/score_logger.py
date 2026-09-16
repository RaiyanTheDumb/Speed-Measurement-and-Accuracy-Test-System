import csv
import json
import os
from datetime import datetime

SCORES_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', 'data', 'scores', 'history.csv')

SCORES_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '..', 'data', 'scores', 'history.json')


def save_score_csv(wpm, accuracy, errors, time_taken, level):
    file_exists = os.path.exists(SCORES_CSV) and os.path.getsize(SCORES_CSV) > 0

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
    """Save score to JSON file"""
    new_entry = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'time_taken': time_taken,
        'wpm': wpm,
        'accuracy': accuracy,
        'errors': errors,
        'level': level
    }

    # Load existing data
    if os.path.exists(SCORES_JSON):
        with open(SCORES_JSON, 'r') as f:
            data = json.load(f)
    else:
        data = []

    # Append new entry
    data.append(new_entry)

    # Save back
    with open(SCORES_JSON, 'w') as f:
        json.dump(data, f, indent=4)


def get_high_score():
    """Get the highest WPM ever recorded"""
    if not os.path.exists(SCORES_CSV):
        return 0

    high = 0
    with open(SCORES_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                if int(row['wpm']) > high:
                    high = int(row['wpm'])
            except:
                pass
    return high


def get_all_scores():
    """Get all scores from CSV as a list"""
    if not os.path.exists(SCORES_CSV):
        return []

    scores = []
    with open(SCORES_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores.append(row)

    return scores