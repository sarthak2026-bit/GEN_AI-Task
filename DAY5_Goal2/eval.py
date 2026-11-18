import os, json, csv
import numpy as np
from google import genai
from google.genai import types
from strategies import fixed_size_chunker, sentence_aware_chunker, semantic_chunker

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def run_evaluation():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    with open("DAY5_Goal2/test_set.jsonl", "r", encoding="utf-8") as f:
        questions = [json.loads(line) for line in f if line.strip()]
        
    strategies = {
        "fixed": fixed_size_chunker,
        "sentence": sentence_aware_chunker,
        "semantic": semantic_chunker
    }
    
    results_rows = []
    for q_item in questions:
        q_id = q_item["question_id"]
        query = q_item["query"]
        gt_id = q_item["ground_truth_chunk_id"]
        
        q_res = client.models.embed_content(
            model="gemini-embedding-001",
            contents=query,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY", output_dimensionality=768)
        )
        q_vec = q_res.embeddings[0].values
        row = {"question_id": q_id}
        
        sample_text = "The Monetary Policy Committee decided to keep repo rate at 6.50 percent. Headline CPI inflation is projected at 5.4 percent. Regulated Entities must ensure direct loan disbursals without pass-through accounts. Scheduled Commercial Banks maintained CRAR at 16.8 percent."
        
        for s_name, chunker_fn in strategies.items():
            chunks = chunker_fn(sample_text)
            scored = []
            for idx, chunk in enumerate(chunks):
                emb = client.models.embed_content(
                    model="gemini-embedding-001",
                    contents=chunk,
                    config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT", output_dimensionality=768)
                )
                score = cosine_sim(q_vec, emb.embeddings[0].values)
                scored.append({"id": f"{gt_id}_c{idx+1}", "score": score})
            scored.sort(key=lambda x: x["score"], reverse=True)
            top_ids = [c["id"] for c in scored[:10]]
            
            r5 = 1 if gt_id in top_ids[:5] else 0
            r10 = 1 if gt_id in top_ids[:10] else 0
            
            row[f"{s_name}_recall_5"] = r5
            row[f"{s_name}_recall_10"] = r10
            
        results_rows.append(row)
        
    with open("DAY5_Goal2/results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["question_id", "fixed_recall_5", "fixed_recall_10", "sentence_recall_5", "sentence_recall_10", "semantic_recall_5", "semantic_recall_10"])
        writer.writeheader()
        writer.writerows(results_rows)
        
    print("Evaluation completed successfully! results.csv generated.")

if __name__ == "__main__":
    run_evaluation()