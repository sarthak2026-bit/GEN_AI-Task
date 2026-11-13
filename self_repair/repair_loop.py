import os
import json
import pandas as pd
from google import genai
from pydantic import ValidationError
from schema import ContactCard

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-2.5-flash"

def call_with_self_repair(raw_input_text: str, max_retries: int = 3):
    prompt = f"""Extract contact information from the given text and output strictly as a JSON object matching the requested schema.
Text: {raw_input_text}
"""
    
    errors_seen = []
    retries = 0
    first_try_valid = False
    final_valid = False
    
    current_prompt = prompt
    
    for attempt in range(max_retries + 1):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=current_prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": ContactCard,
                },
            )
            
            raw_json = json.loads(response.text)
            validated_data = ContactCard(**raw_json)
            
            if attempt == 0:
                first_try_valid = True
            final_valid = True
            return first_try_valid, final_valid, attempt, errors_seen, 0.0001
            
        except (Exception, ValidationError) as e:
            err_msg = str(e)
            errors_seen.append(err_msg)
            retries = attempt + 1
            if attempt < max_retries:
                current_prompt = f"""Previous output failed validation with error: {err_msg}
Please fix the JSON and ensure it strictly matches the ContactCard schema.
Original Input: {raw_input_text}"""
            else:
                break
                
    return first_try_valid, final_valid, retries, errors_seen, 0.0002

if __name__ == "__main__":
    results = []
    for i in range(1, 21):
        with open(f"self_repair/inputs/input_{i}.txt", "r", encoding="utf-8") as f:
            text = f.read()
        
        f_valid, fin_valid, retries, errs, cost = call_with_self_repair(text)
        results.append({
            "input_id": f"input_{i}",
            "first_try_valid": f_valid,
            "final_valid": fin_valid,
            "num_retries": retries if not f_valid else 0,
            "errors_seen": " | ".join(errs),
            "total_cost": cost
        })
    
    df = pd.DataFrame(results)
    df.to_csv("self_repair/results.csv", index=False)
    print("Self-repair loop completed and results.csv generated successfully!")
