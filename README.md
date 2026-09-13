# Mood Detector 🧠

A small Flask web app I built for the Python Lab assignment. You type in a sentence about how you're feeling, and it figures out your mood from the words and phrases you use — then shows you an emoji, a little reaction message, and keeps a history of everything you've logged.

## What it actually does

Type something like *"I passed my exam today"* into the box and hit submit. The app reads your sentence, checks it against lists of mood-related words and phrases (things like "happy", "passed my exam", "so stressed", "can't sleep"), and picks whichever mood matches best. It then shows:

- The detected mood with a matching emoji
- A short, human reaction line (so it feels like the app is actually responding to you, not just labeling you)
- Your full history of past entries, with timestamps
- A bar chart showing how often each mood has come up

There's also a "Clear" button to wipe the history and start fresh.

## Why I built it this way

The assignment asked for a Flask frontend project referencing the [W3Schools Python/Flask tutorial](https://www.w3schools.com/python/), so I kept it to the core things that tutorial covers:

- **Routes** (`/`, `/log`, `/clear`) to handle showing the page, logging a mood, and clearing history
- **Jinja2 templates** with `base.html` as the shared layout and `index.html` extending it, so the header/footer don't get repeated
- **Forms and POST requests** to send what you typed to the server
- **Static files** for the CSS, linked the proper Flask way with `url_for`

The mood detection itself is simple on purpose — it's just checking if certain words or short phrases appear in your text, no external AI or machine learning involved. Multi-word phrases (like "passed my exam") count for more than single generic words (like "good"), so the app leans toward picking up on specific situations rather than just vague positive/negative words.

## Tech used

- **Python + Flask** for the backend and routing
- **Jinja2** for templating
- **HTML/CSS** for the frontend
- **Chart.js** (loaded from a CDN) for the mood history bar chart

## Project structure

```
mood_detector/
├── app.py                 # Flask app: routes + mood detection logic
├── requirements.txt        # Just Flask
├── templates/
│   ├── base.html           # Shared page layout
│   └── index.html          # Main page (form, result, history, chart)
└── static/
    └── style.css            # All the styling
```

## How to run it yourself

1. Make sure Python is installed.
2. Install the one dependency:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open the link it gives you (usually `http://127.0.0.1:5000`) in a browser.

## A couple of honest notes
- Mood history is stored in memory (a plain Python list), not a database — so it resets if the server restarts. Fine for a class demo, but wouldn't survive a real deployment long-term.
- The mood detection is keyword/phrase-based, not real natural language understanding — it won't catch sarcasm or anything outside the word lists I defined.
