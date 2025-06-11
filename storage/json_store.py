import json
from pathlib import Path

DATA_FILE = Path("flashcards.json")

def save_flashcards(cards):
    with open(DATA_FILE, "w") as f:
        json.dump(cards, f, indent=2)

def load_flashcards():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
