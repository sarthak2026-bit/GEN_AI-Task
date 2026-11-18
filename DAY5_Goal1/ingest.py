import os, json, csv
from pypdf import PdfReader
from google import genai
from google.genai import types

def chunk_text(text, chunk_size=100, overlap=20):
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

def run_ingestion():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is missing!")
    client = genai.Client(api_key=api_key)
    pdf_dir = os.path.join("DAY5_Goal1", "corpus_pdfs")
    vector_store = []
    manifest_rows = [["doc_id", "title", "year", "doc_type", "num_pages", "num_chunks"]]
    
    for filename in sorted(os.listdir(pdf_dir)):
        if not filename.endswith(".pdf"):
            continue
        parts = filename.replace(".pdf", "").split("__")
        doc_id, year, doc_type = parts[0], int(parts[1]), parts[2].replace("_", " ")
        filepath = os.path.join(pdf_dir, filename)
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        title = reader.pages[0].extract_text().split("\n")[0]
        doc_chunks = 0
        
        for p_idx, page in enumerate(reader.pages):
            chunks = chunk_text(page.extract_text() or "")
            for c_idx, c_str in enumerate(chunks):
                res = client.models.embed_content(
                    model="gemini-embedding-001",
                    contents=c_str,
                    config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT", output_dimensionality=768)
                )
                vector_store.append({
                    "chunk_id": f"{doc_id}_p{p_idx+1}_c{c_idx+1}",
                    "text": c_str,
                    "embedding": res.embeddings[0].values,
                    "metadata": {"doc_id": doc_id, "title": title, "year": year, "doc_type": doc_type, "page_number": p_idx + 1}
                })
                doc_chunks += 1
        manifest_rows.append([doc_id, title, year, doc_type, num_pages, doc_chunks])
        print(f"Indexed {doc_id} -> {doc_chunks} chunks embedded.")
        
    with open("DAY5_Goal1/vector_index.json", "w", encoding="utf-8") as f:
        json.dump(vector_store, f)
    with open("DAY5_Goal1/corpus_manifest.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(manifest_rows)
    print(f"Ingestion Complete! Total vectors indexed: {len(vector_store)}")

if __name__ == "__main__":
    run_ingestion()
