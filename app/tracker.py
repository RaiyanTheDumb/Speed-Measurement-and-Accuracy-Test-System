"""
tracker.py
Tracks and analyzes typing errors during a test session.
"""


def track_errors(sample_text, typed_text):
    """
    Track detailed error information for each mistake.

    Compares typed text against sample text character
    by character and records each error's position,
    expected character, and actual typed character.

    Args:
        sample_text (str): The original sample text.
        typed_text (str): The text typed by the user.

    Returns:
        list: List of dicts with keys:
              'position', 'expected', 'typed'
    """
    errors = []
    total = min(len(sample_text), len(typed_text))

    for i in range(total):
        if sample_text[i] != typed_text[i]:
            errors.append({
                'position': i,
                'expected': sample_text[i],
                'typed': typed_text[i]
            })

    return errors


def count_errors(sample_text, typed_text):
    """
    Count total number of typing errors.

    Args:
        sample_text (str): The original sample text.
        typed_text (str): The text typed by the user.

    Returns:
        int: Total number of errors found.
    """
    return len(track_errors(sample_text, typed_text))