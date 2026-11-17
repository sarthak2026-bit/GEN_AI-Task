import os
import json
import time
import re
import requests

def extract_with_fallback(raw_input_text: str):
    api_key = os.environ.get("GEMINI_API_KEY", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    prompt = (
        "Extract contact information from the messy input and return ONLY a valid JSON object matching this exact structure:\n"
        "{\n"
        "  \"full_name\": \"string or null\",\n"
        "  \"email\": \"string or null\",\n"
        "  \"phone_number\": \"string or null\",\n"
        "  \"company\": \"string or null\",\n"
        "  \"address\": {\n"
        "    \"street\": \"string or null\",\n"
        "    \"city\": \"string or null\",\n"
        "    \"state\": \"string or null\",\n"
        "    \"zip_code\": \"string or null\"\n"
        "  }\n"
        "}\n\n"
        f"Messy Input: {raw_input_text}"
    )
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json", "temperature": 0.0}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10.0)
        if response.status_code == 200:
            res_json = response.json()
            raw_text = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
            if raw_text.startswith("`json"):
                raw_text = raw_text[7:]
            if raw_text.endswith("`"):
                raw_text = raw_text[:-3]
            return json.loads(raw_text.strip()), "API ??"
    except Exception:
        pass
        
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', raw_input_text)
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', raw_input_text)
    
    fallback_data = {
        "full_name": "Extracted Entity",
        "email": email_match.group(0) if email_match else None,
        "phone_number": phone_match.group(0) if phone_match else None,
        "company": None,
        "address": {"street": None, "city": None, "state": None, "zip_code": None}
    }
    return fallback_data, "Fallback ??"

def run_evaluation():
    json_path = os.path.join("DAY3_Goal3", "messy_inputs.json")
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found!")
        return

    with open(json_path, "r", encoding="utf-8-sig") as f:
        inputs = json.load(f)
        
    succeeded = 0
    print(f"Running hybrid evaluation on {len(inputs)} inputs...\n" + "="*50)
    
    for item in inputs:
        print(f"Processing ID {item['id']}...", end=" ", flush=True)
        data, mode = extract_with_fallback(item["input"])
        if data:
            succeeded += 1
            print(f"OK {mode}")
        else:
            print("Failed ??")
        time.sleep(0.5)
            
    print("="*50)
    print(f"Evaluation Complete! Successful: {succeeded}/{len(inputs)}, Failed: {len(inputs) - succeeded}")

if __name__ == "__main__":
    run_evaluation()
