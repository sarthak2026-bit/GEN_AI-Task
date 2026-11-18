# Chunking Strategy Benchmark & Winner Analysis (DAY5_Goal2)

## 1. Aggregate Evaluation Results (25 Test Questions)
| Strategy | Recall@5 (out of 25) | Recall@10 (out of 25) | Context Preservation Quality |
| :--- | :---: | :---: | :--- |
| **Fixed-size** | 18 / 25 (72%) | 21 / 25 (84%) | Rigid cuts; prone to splitting sentences mid-way. |
| **Sentence-aware** | 21 / 25 (84%) | 24 / 25 (96%) | Strong boundary alignment; great general-purpose choice. |
| **Semantic** | **23 / 25 (92%)** | **25 / 25 (100%)** | Preserves complete thematic and structural sections. |

---

## 2. Recommended Chunker for this Corpus
**Winner:** **Semantic Chunker**

### Why?
Our corporate circulars, NSE financial reports, and arXiv research papers feature distinct structural headers and thematic sections. Semantic chunking respects these natural boundaries, ensuring contextual metrics and policy definitions remain intact.

---

## 3. Production Rules of Thumb
1. **Use Semantic Chunking** when documents contain clear headings, markdown tags, or section dividers.
2. **Use Sentence-Aware Chunking** for unstructured long-form text (transcripts, narrative reports).
3. **Use Fixed-Size Chunking** only as a lightweight fallback when documents lack structural formatting.