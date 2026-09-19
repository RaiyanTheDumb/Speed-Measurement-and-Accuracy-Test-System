# Docstrings Guide

## Python Files

### app/__init__.py
- `create_app()` — Creates and returns configured Flask app

### app/calculator.py
- `calculate_wpm(typed_text, time_seconds)` — Returns WPM score
- `calculate_accuracy(sample_text, typed_text)` — Returns accuracy %
- `calculate_errors(sample_text, typed_text)` — Returns error count
- `get_typing_level(wpm)` — Returns level string

### app/text_loader.py
- `load_sample_text()` — Returns random sample text string

### app/tracker.py
- `track_errors(sample_text, typed_text)` — Returns list of error dicts
- `count_errors(sample_text, typed_text)` — Returns total error count

### app/score_logger.py
- `save_score_csv(...)` — Saves score to CSV file
- `save_score_json(...)` — Saves score to JSON file
- `get_high_score()` — Returns highest WPM recorded
- `get_all_scores()` — Returns all scores as list

### app/routes.py
- `index()` — Renders main typing test page
- `calculate()` — API endpoint, returns JSON results
- `history()` — Renders score history page

## JavaScript Files

### timer.js
- `startTimer()` — Starts interval, increments seconds
- `stopTimer()` — Clears interval
- `resetTimer()` — Resets seconds to 0

### highlighter.js
- `highlightChars()` — Applies correct/incorrect CSS classes
- `resetHighlights()` — Removes all highlight classes

### dashboard.js
- `showDashboard(wpm, accuracy, errors, timeTaken, level)` — Shows modal
- `hideDashboard()` — Hides modal

### keyboard.js
- `sendResults(typedText, sampleText)` — POSTs data to /calculate