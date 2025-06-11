# ui/gradio_app.py
import gradio as gr
from core.extractor import extract_text_from_pdf
from core.chunker import chunk_text
from core.card_generator import generate_cards_from_chunk, parse_flashcards

def process_pdf(file):
    text = extract_text_from_pdf(file.name)
    chunks = chunk_text(text)
    all_cards = []
    for chunk in chunks:
        raw = generate_cards_from_chunk(chunk)
        parsed = parse_flashcards(raw)
        all_cards.extend(parsed)
    return all_cards

iface = gr.Interface(fn=process_pdf,
                     inputs=gr.File(label="Upload PDF"),
                     outputs=gr.Dataframe(headers=["question", "answer"]),
                     title="PDF Flashcard Generator")

iface.launch()
