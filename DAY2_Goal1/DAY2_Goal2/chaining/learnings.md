# Prompt Chaining Learnings & Error Analysis

## 1. What Broke During Testing & Edge Cases
- **Silent Error Propagation (Garbage In, Garbage Out):** When testing malformed or vague briefs in Step 1, if `target_audience` or `key_features` were extracted inaccurately (e.g., hallucinating a feature or misclassifying the category), Step 2 did **not** crash. Because Step 2 received valid JSON syntax, it happily generated polished, persuasive ad copy around the wrong facts.
- **Superlative Leakage in Step 2:** At `temperature=0.3` or higher, Step 2 occasionally slipped words like "best" or "ultimate" into headlines when trying to sound creative. Step 3 reliably caught these violations against `brand_rules.md` and disqualified those variants.
- **API Rate Limits & Transient 503 Errors:** Chaining 3 sequential LLM calls across 5 briefs equals 15 API requests in rapid succession, triggering `429 Resource Exhausted` errors without exponential backoff and polite delays.

## 2. How Step 1 Errors Affected Step 2
- **Syntactic vs. Semantic Failure:** Using `response_schema` (Pydantic) eliminated 100% of JSON parsing crashes between Step 1 and Step 2. However, schema enforcement only guarantees *structure*, not *truthfulness*.
- **Fix Applied:** Adding strict grounding instructions in `extract.txt` (*"Be strictly factual based only on the provided text"*) and saving every intermediate JSON file (`step1_attributes.json`, `step2_variants.json`, `step3_winner.json`) made debugging effortless—allowing us to pinpoint whether a bad final ad came from a bad extraction or weak copywriting.

## 3. Key Takeaways on Splitting Tasks into Smaller Prompts
1. **Single Responsibility Principle for Prompts:** Separating *fact extraction*, *creative generation*, and *rule-based critique* prevents the model from losing focus. Asking one prompt to extract facts, write 3 ads, and self-police brand rules simultaneously caused rule violations to slip through.
2. **Independent Tunability:** Each step can use different constraints—Step 1 focuses on strict extraction, Step 2 focuses on creative variety, and Step 3 acts as a deterministic compliance gatekeeper.
3. **Auditability:** Saving intermediate artifacts (`run_1` to `run_5`) creates an observable trace, which is essential for production creative tools like PocketStudio.
