from core.extractor import extract_text_from_pdf
from core.chunker import chunk_text
from core.card_generator import generate_cards_from_chunk, parse_flashcards
from storage.json_store import save_flashcards, load_flashcards


def main():
    path = input("Enter PDF path: ")
    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)

    all_cards = []
    for chunk in chunks:
        print("Generating cards for chunk...")
        raw_output = generate_cards_from_chunk(chunk)
        print("LLM output\n : ", raw_output)

        parsed_cards = parse_flashcards(raw_output)
        all_cards.extend(parsed_cards)  # Save only parsed Q&A pairs

    save_flashcards(all_cards)
    print("Flashcards saved!")

if __name__ == "__main__":
    main()
