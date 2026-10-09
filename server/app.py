import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://sunilkumawat-ai.github.io"])

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemma-4-26b-a4b-it"
URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
       + MODEL + ":generateContent")

PROMPT = (
    "You are TrailShield, a cautious outdoor assistant. Look at this "
    "photo from a trail. In under 60 words: start with a short title in "
    "capitals (e.g. POSSIBLE OBSTRUCTION), say what the image appears "
    "to show, and give one 'Consider...' recommendation. Never say "
    "something is definitely safe or definitely dangerous. Use words "
    "like 'possible' and 'appears'. End with: Use your judgment."
)

@app.get("/")
def health():
    return "TrailShield server is running"

@app.post("/check")
def check():
    data = request.get_json(silent=True) or {}
    image = data.get("image")
    if not image:
        return jsonify(error="no image"), 400
    body = {"contents": [{"parts": [
        {"text": PROMPT},
        {"inline_data": {"mime_type": "image/jpeg", "data": image}},
    ]}]}
    r = requests.post(URL, headers={"x-goog-api-key": API_KEY},
                      json=body, timeout=90)
    if r.status_code != 200:
        return jsonify(error="AI request failed", status=r.status_code), 502
    parts = r.json()["candidates"][0]["content"]["parts"]
    text = " ".join(p["text"] for p in parts
                    if "text" in p and not p.get("thought"))
    return jsonify(result=text)
