import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

def generate_cards_from_chunk(chunk: str):
    url = "https://api.together.xyz/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    You are a helpful AI tutor. Create 2-3 flashcards (in Q&A format) from the following content only:

    {chunk}

    Format:
    Q: ...
    A: ...
    """

    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512,
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"Together API error {response.status_code}: {response.text}")
    


def parse_flashcards(llm_output: str):
    cards = []
    lines = llm_output.strip().split("\n")
    current_q = None
    current_a = None

    for line in lines:
        if line.strip().startswith("Q:"):
            if current_q and current_a:
                cards.append({"question": current_q.strip(), "answer": current_a.strip()})
            current_q = line.replace("Q:", "").strip()
            current_a = None
        elif line.strip().startswith("A:"):
            current_a = line.replace("A:", "").strip()
        elif current_a is not None:
            current_a += " " + line.strip()

    if current_q and current_a:
        cards.append({"question": current_q.strip(), "answer": current_a.strip()})

    return cards


if __name__ == "__main__":
    sample_chunk = "Photosynthesis is a process used by plants to convert light energy into chemical energy."
    raw_output = generate_cards_from_chunk(sample_chunk)
    print("LLM Raw Output:\n", raw_output)

    structured_cards = parse_flashcards(raw_output)
    print("\nParsed Flashcards:")
    for card in structured_cards:
        print(f"Q: {card['question']}\nA: {card['answer']}\n")
