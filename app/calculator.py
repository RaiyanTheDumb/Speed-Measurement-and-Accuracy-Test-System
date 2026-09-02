def calculate_wpm(typed_text, time_seconds):
    """
    WPM = (Total characters typed / 5) / time in minutes
    Standard: 1 word = 5 characters
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
    Accuracy = (Correct characters / Total characters) * 100
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
    Errors = number of wrong characters typed
    """
    errors = 0
    total = min(len(sample_text), len(typed_text))

    for i in range(total):
        if sample_text[i] != typed_text[i]:
            errors += 1

    errors += abs(len(typed_text) - len(sample_text))

    return errors