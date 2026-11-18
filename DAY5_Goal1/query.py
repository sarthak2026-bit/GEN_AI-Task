import os, json
import numpy as np
from google import genai
from google.genai import types

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

class VectorSearchEngine:
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is required!")
        self.client = genai.Client(api_key=api_key)
        with open("DAY5_Goal1/vector_index.json", "r", encoding="utf-8") as f:
            self.index = json.load(f)
            
    def search(self, query, filters=None, top_k=5):
        res = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=query,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY", output_dimensionality=768)
        )
        q_vec = res.embeddings[0].values
        hits = []
        for item in self.index:
            meta = item["metadata"]
            if filters and any(meta.get(k) != v for k, v in filters.items()):
                continue
            score = cosine_sim(q_vec, item["embedding"])
            hits.append({"chunk_id": item["chunk_id"], "score": round(score, 4), "metadata": meta, "text": item["text"][:150] + "..."})
        hits.sort(key=lambda x: x["score"], reverse=True)
        return hits[:top_k]

def run_queries():
    engine = VectorSearchEngine()
    queries = [
        {"q": "Inflation projection and repo rate decision", "filter": {"year": 2023, "doc_type": "RBI Circular"}},
        {"q": "Banks GNPA and capital buffers performance", "filter": {"year": 2024, "doc_type": "RBI Circular"}},
        {"q": "Digital lending and video KYC guidelines", "filter": {"doc_type": "RBI Circular"}},
        {"q": "Offline digital payments in low connectivity areas", "filter": {"year": 2022}},
        {"q": "Retail SIPs and DIIs vs FPI outflows", "filter": {"year": 2022, "doc_type": "NSE Report"}},
        {"q": "Index options and mid-cap equity growth", "filter": {"year": 2023, "doc_type": "NSE Report"}},
        {"q": "Sustainability reporting and ESG compliance", "filter": {"year": 2024, "doc_type": "NSE Report"}},
        {"q": "Why dense embeddings beat BM25 keyword search", "filter": {"doc_type": "arXiv Paper"}},
        {"q": "Optimal token chunk size and overlap for RAG", "filter": {"year": 2023, "doc_type": "arXiv Paper"}},
        {"q": "Reciprocal Rank Fusion in hybrid search", "filter": {"year": 2024, "doc_type": "arXiv Paper"}}
    ]
    md = ["# Filtered Semantic Search Evaluation (DAY5_Goal1)\n"]
    for idx, item in enumerate(queries, 1):
        results = engine.search(item["q"], filters=item["filter"], top_k=5)
        print(f"Query {idx} Top Match: {results[0]['chunk_id']} ({results[0]['score']})")
        md.append(f"### {idx}. {item['q']}\n- **Filter:** `{json.dumps(item['filter'])}`\n- **Top Results:**")
        for r_idx, r in enumerate(results, 1):
            md.append(f"  {r_idx}. `{r['chunk_id']}` (Score: `{r['score']}` | {r['metadata']['doc_type']}, {r['metadata']['year']}, Page {r['metadata']['page_number']}): *{r['text']}*")
        md.append("")
    with open("DAY5_Goal1/filtered_queries.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("Saved filtered_queries.md successfully!")

if __name__ == "__main__":
    run_queries()
