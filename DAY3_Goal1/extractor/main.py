import os
import sys
import json
import time
import pandas as pd
from google import genai
from google.genai import types

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from schema import InvoiceExtractionSchema

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-3.5-flash-lite"

def extract_document(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8-sig") as f:
        doc_content = f.read()
        
    prompt = f"""
You are an expert document data extraction engine. Extract all structured fields accurately from the following invoice document text according to the required schema.

Document Content:
{doc_content}
"""
    max_retries = 5
    delay = 10
    for attempt in range(max_retries):
        try:
            resp = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=InvoiceExtractionSchema,
                    temperature=0.0
                )
            )
            time.sleep(2)
            return json.loads(resp.text)
        except Exception as e:
            print(f"API Error on {file_path}: {e}. Retrying in {delay}s...")
            time.sleep(delay)
            delay *= 1.5
    raise Exception(f"Failed to extract {file_path} after max retries.")

def evaluate_all():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    samples_dir = os.path.join(base_dir, "samples")
    gt_path = os.path.join(base_dir, "ground_truth.jsonl")
    
    gt_list = []
    with open(gt_path, "r", encoding="utf-8-sig") as f:
        for line in f:
            if line.strip():
                gt_list.append(json.loads(line))
                
    results = []
    
    for i in range(1, 11):
        sample_id = f"sample_{i}"
        file_path = os.path.join(samples_dir, f"{sample_id}.txt")
        print(f"Processing {sample_id}...")
        
        extracted = extract_document(file_path)
        gt = gt_list[i-1]
        
        fields_to_check = [
            ("invoice_number", extracted.get("invoice_number"), gt.get("invoice_number")),
            ("vendor_name", extracted.get("vendor_name"), gt.get("vendor_name")),
            ("customer_name", extracted.get("customer_name"), gt.get("customer_name")),
            ("invoice_date", extracted.get("invoice_date"), gt.get("invoice_date")),
            ("status", extracted.get("status"), gt.get("status")),
            ("billing_address.street", extracted.get("billing_address", {}).get("street"), gt.get("billing_address", {}).get("street")),
            ("billing_address.city", extracted.get("billing_address", {}).get("city"), gt.get("billing_address", {}).get("city")),
            ("billing_address.pin_code", extracted.get("billing_address", {}).get("pin_code"), gt.get("billing_address", {}).get("pin_code")),
            ("discount_applied", extracted.get("discount_applied"), gt.get("discount_applied")),
            ("total_amount", extracted.get("total_amount"), gt.get("total_amount"))
        ]
        
        for field_name, ext_val, gt_val in fields_to_check:
            match = (ext_val == gt_val)
            results.append({
                "sample_id": sample_id,
                "field_name": field_name,
                "extracted_value": str(ext_val),
                "ground_truth_value": str(gt_val),
                "exact_match": match
            })
            
    df = pd.DataFrame(results)
    out_csv = os.path.join(base_dir, "field_accuracy.csv")
    df.to_csv(out_csv, index=False)
    print(f"Evaluation complete! field_accuracy.csv successfully created at {out_csv}.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) > 1:
        path = sys.argv[1]
        res = extract_document(path)
        print(json.dumps(res, indent=2))
    else:
        evaluate_all()

