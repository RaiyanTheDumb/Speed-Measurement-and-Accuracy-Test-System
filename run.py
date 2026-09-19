"""
run.py
Entry point for the Typing Speed Test Flask application.
Run this file to start the development server.
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)