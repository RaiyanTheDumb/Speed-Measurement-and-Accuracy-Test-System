# ⌨️ Typing Speed Measurement and Accuracy Test System

A web-based typing speed test application built with Python and Flask.
Measures Words Per Minute (WPM), accuracy percentage, and error count
in real time with visual feedback.

---

## Features
- 📝 Random sample text loaded for each test
- ⏱️ Auto-starting timer on first keypress
- 🟢🔴 Real-time character highlighting (green/red)
- 💨 WPM, accuracy and error calculation
- 🏅 Typing level rating (Beginner to Expert)
- 📊 Performance dashboard modal on completion
- 💾 Score history saved to CSV and JSON
- 📋 Score history page with high score tracking

---

## Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML, CSS, JavaScript (Vanilla) |
| Storage | CSV, JSON (local) |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```
Speed-Measurement-and-Accuracy-Test-System/
│
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # URL routes and API endpoints
│   ├── calculator.py        # WPM, accuracy, error math
│   ├── text_loader.py       # Random text loader
│   ├── tracker.py           # Error tracking
│   └── score_logger.py      # CSV/JSON score saving
│
├── static/
│   ├── css/
│   │   └── style.css        # Styling
│   └── js/
│       ├── timer.js         # Timer logic
│       ├── keyboard.js      # Keypress detection
│       ├── highlighter.js   # Real-time highlighting
│       └── dashboard.js     # Results modal
│
├── templates/
│   ├── base.html            # Base layout
│   ├── index.html           # Main test page
│   └── history.html         # Score history page
│
├── data/
│   ├── texts/
│   │   └── samples.json     # Sample typing texts
│   └── scores/
│       └── history.csv      # Score history
│
├── tests/
│   ├── test_calculator.py   # Unit tests
│   ├── test_edge_cases.py   # Edge case tests
│   └── test_routes.py       # Route tests
│
├── docs/
│   └── docstrings_guide.md  # Documentation guide
│
├── config.py                # App configuration
├── run.py                   # Entry point
└── requirements.txt         # Dependencies
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/RaiyanTheDumb/Speed-Measurement-and-Accuracy-Test-System.git
cd Speed-Measurement-and-Accuracy-Test-System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python run.py
```

### 4. Open in browser
http://127.0.0.1:5000


---

## How to Use
1. Open the app in your browser
2. Start typing the sample text in the input box
3. Timer starts automatically on first keypress
4. Characters highlight green ✅ or red ❌ in real time
5. When done, results modal shows WPM, accuracy and level
6. Click **View History** to see all past scores

---

## Typing Levels
| WPM | Level |
|---|---|
| 0 – 30 | 🐢 Beginner |
| 31 – 50 | 📝 Average |
| 51 – 75 | ✅ Fluent |
| 76 – 100 | ⚡ Fast |
| 100+ | 🏆 Expert |

---

## Module Map
| File | Role |
|---|---|
| `calculator.py` | WPM and accuracy math |
| `text_loader.py` | Loads random sample texts |
| `tracker.py` | Tracks error positions |
| `score_logger.py` | Saves and retrieves scores |
| `timer.js` | Live countdown timer |
| `keyboard.js` | Keypress and input detection |
| `highlighter.js` | Real-time color feedback |
| `dashboard.js` | Results modal display |