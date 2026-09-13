from flask import Flask, render_template, request, redirect, url_for  # type: ignore[import-not-found]
from datetime import datetime

app = Flask(__name__)

mood_words = {
    "Happy": [
        "happy", "great", "good", "joy", "awesome", "glad", "smiling",
        "passed my exam", "passed the exam", "got good marks", "aced it",
        "got selected", "got the job", "got promoted", "achieved my goal",
        "made it happen", "proud of myself", "everything worked out",
    ],
    "Excited": [
        "excited", "thrilled", "pumped", "energetic", "can't wait",
        "cant wait", "so hyped", "best day ever", "winning", "we won",
    ],
    "Sad": [
        "sad", "down", "low", "upset", "cry", "crying", "unhappy",
        "failed my exam", "failed the exam", "lost my", "let down",
        "heartbroken", "missing them", "nothing feels right",
        "breaking down", "so lonely", "so lost", "so empty", "so hopeless","break up"
    ],
    "Angry": [
        "angry", "mad", "frustrated", "annoyed", "furious", "fed up",
        "so unfair", "sick of this", "can't stand", "cant stand",
    ],
    "Anxious": [
        "anxious", "nervous", "worried", "stressed", "overwhelmed",
        "exam tomorrow", "running out of time", "what if i fail",
        "can't sleep", "cant sleep", "so much pressure",
    ],
    "Calm": [
        "calm", "relaxed", "peaceful", "fine", "chill", "at ease",
        "taking it slow", "nothing to worry about", "content",
    ],
}

mood_emojis = {
    "Happy": "😄",
    "Excited": "🤩",
    "Sad": "😢",
    "Angry": "😠",
    "Anxious": "😰",
    "Calm": "😌",
    "Neutral": "😐",
}

mood_messages = {
    "Happy": "That's wonderful, this really sounds like a happy moment for you!",
    "Excited": "Your excitement is coming through loud and clear!",
    "Sad": "That sounds heavy, sending you comfort right now.",
    "Angry": "That sounds really frustrating, it's okay to feel this way.",
    "Anxious": "It sounds like a lot is on your mind, take a breath if you can.",
    "Calm": "Nice, sounds like you're in a peaceful headspace.",
    "Neutral": "Thanks for sharing, tell me a bit more about how you feel.",
}

history = []


def detect_mood(text):
    text = text.lower()
    best_mood = "Neutral"
    best_score = 0

    for mood in mood_words:
        score = 0
        for phrase in mood_words[mood]:
            if phrase in text:
                score += len(phrase.split())
        if score > best_score:
            best_score = score
            best_mood = mood

    return best_mood, mood_emojis[best_mood], mood_messages[best_mood]


@app.route("/")
def home():
    mood_counts = {}
    for entry in history:
        mood_counts[entry["mood"]] = mood_counts.get(entry["mood"], 0) + 1

    return render_template("index.html", history=list(reversed(history)), mood_counts=mood_counts)


@app.route("/log", methods=["POST"])
def log_mood():
    text = request.form.get("mood_text", "").strip()
    if text:
        mood, emoji, message = detect_mood(text)
        history.append({
            "text": text,
            "mood": mood,
            "emoji": emoji,
            "message": message,
            "time": datetime.now().strftime("%d %b, %I:%M %p"),
        })
    return redirect(url_for("home"))


@app.route("/clear", methods=["POST"])
def clear_history():
    history.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)