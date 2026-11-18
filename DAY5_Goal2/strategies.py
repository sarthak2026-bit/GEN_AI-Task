import re

def fixed_size_chunker(text: str, chunk_size: int = 100, overlap: int = 20) -> list[str]:
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start += (chunk_size - overlap)
    return chunks

def sentence_aware_chunker(text: str, target_chunk_size: int = 100) -> list[str]:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = []
    current_word_count = 0
    for sentence in sentences:
        words = sentence.split()
        if current_word_count + len(words) > target_chunk_size and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_word_count = len(words)
        else:
            current_chunk.append(sentence)
            current_word_count += len(words)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def semantic_chunker(text: str) -> list[str]:
    sections = re.split(r'\n(?=Section|\b[A-Z][a-z]+ [A-Z][a-z]+\b)', text)
    chunks = [s.strip() for s in sections if s.strip()]
    return chunks if chunks else [text]