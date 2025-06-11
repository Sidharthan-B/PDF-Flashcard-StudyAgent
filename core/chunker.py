def chunk_text(text: str, max_words=150):
    import re
    paragraphs = re.split(r"\n{2,}", text)
    chunks = []
    for para in paragraphs:
        words = para.split()
        if len(words) > max_words:
            for i in range(0, len(words), max_words):
                chunks.append(" ".join(words[i:i+max_words]))
        elif words:
            chunks.append(para.strip())
    return chunks
