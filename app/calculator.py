"""
calculator.py
Core math algorithms for WPM, Accuracy, Errors and Typing Level.
"""


def calculate_wpm(typed_text, time_seconds):
    """
    Calculate Words Per Minute (WPM).

    Uses the standard formula where 1 word = 5 characters.
    Formula: (total characters / 5) / time in minutes

    Args:
        typed_text (str): The text typed by the user.
        time_seconds (int): Time taken in seconds.

    Returns:
        int: WPM score. Returns 0 if time is 0 or less.
    """
    if time_seconds <= 0:
        return 0

    total_chars = len(typed_text)
    words = total_chars / 5
    time_minutes = time_seconds / 60
    wpm = round(words / time_minutes)

    return wpm


def calculate_accuracy(sample_text, typed_text):
    """
    Calculate typing accuracy as a percentage.

    Compares each character of typed text against
    the sample text position by position.

    Args:
        sample_text (str): The original sample text.
        typed_text (str): The text typed by the user.

    Returns:
        int: Accuracy percentage (0-100).
             Returns 0 if typed text is empty.
    """
    if len(typed_text) == 0:
        return 0

    correct = 0
    total = min(len(sample_text), len(typed_text))

    for i in range(total):
        if sample_text[i] == typed_text[i]:
            correct += 1

    accuracy = round((correct / len(sample_text)) * 100)

    return min(accuracy, 100)


def calculate_errors(sample_text, typed_text):
    """
    Count the total number of typing errors.

    Compares each character position and counts
    mismatches. Extra characters beyond sample
    length also count as errors.

    Args:
        sample_text (str): The original sample text.
        typed_text (str): The text typed by the user.

    Returns:
        int: Total number of errors.
    """
    errors = 0
    total = min(len(sample_text), len(typed_text))

    for i in range(total):
        if sample_text[i] != typed_text[i]:
            errors += 1

    errors += abs(len(typed_text) - len(sample_text))

    return errors


def get_typing_level(wpm):
    """
    Determine typing level based on WPM score.

    Levels:
        0-30   → Beginner
        31-50  → Average
        51-75  → Fluent
        76-100 → Fast
        100+   → Expert

    Args:
        wpm (int): Words per minute score.

    Returns:
        str: Typing level label.
    """
    if wpm <= 30:
        return 'Beginner'
    elif wpm <= 50:
        return 'Average'
    elif wpm <= 75:
        return 'Fluent'
    elif wpm <= 100:
        return 'Fast'
    else:
        return 'Expert'