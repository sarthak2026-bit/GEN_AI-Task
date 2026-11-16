# Structured Output Document Extractor (Day 3 Goal 1)

Extracts structured JSON data from invoices using Gemini API (`gemini-3.5-flash-lite`) and Pydantic validation schemas.

## Deliverables
- `schema.py`: Pydantic model with nested objects, lists, enums, and optional fields.
- `samples/`: 10 synthetic invoice text documents.
- `ground_truth.jsonl`: Expected JSON output for evaluation.
- `main.py`: CLI tool and automated batch evaluation script.
- `field_accuracy.csv`: Field-by-field accuracy comparison.
- `accuracy_summary.md`: Performance analysis and error breakdown.

## Usage Instructions
1. Run batch evaluation:
   ```powershell
   py DAY3_Goal1/extractor/main.py
@'
# Structured Output Document Extractor (Day 3 Goal 1)

Extracts structured JSON data from invoices using Gemini API (gemini-3.5-flash-lite) and Pydantic validation schemas.

## Deliverables
- schema.py: Pydantic model with nested objects, lists, enums, and optional fields.
- samples/: 10 synthetic invoice text documents.
- ground_truth.jsonl: Expected JSON output for evaluation.
- main.py: CLI tool and automated batch evaluation script.
- field_accuracy.csv: Field-by-field accuracy comparison.
- accuracy_summary.md: Performance analysis and error breakdown.

## Usage Instructions
1. Run batch evaluation:
   py DAY3_Goal1/extractor/main.py

2. Extract a single document via CLI:
   py DAY3_Goal1/extractor/main.py DAY3_Goal1/extractor/samples/sample_1.txt
