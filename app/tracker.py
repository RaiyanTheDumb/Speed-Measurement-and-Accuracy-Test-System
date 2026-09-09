def track_errors(sample_text, typed_text):
    """
    Returns a list of error positions and details
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
    Returns total number of errors
    """
    return len(track_errors(sample_text, typed_text))