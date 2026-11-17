# Vision Document Extractor: Quality & Accuracy Report (DAY4_Goal2)

## 1. Executive Summary
This report evaluates the performance of the multimodal Gemini-powered document extraction pipeline across 10 test samples categorized into four distinct real-world quality buckets: **Clean**, **Rotated**, **Dark (Low-Light)**, and **Blurry**.

## 2. Accuracy Breakdown by Quality Bucket

| Quality Bucket | Sample Count | Avg Fields Correct / Total | Accuracy Rate | Avg Confidence Score |
|----------------|--------------|---------------------------|---------------|----------------------|
| **Clean**      | 3            | 4.0 / 4                   | 100%          | 0.98                 |
| **Rotated**    | 3            | 3.67 / 4                  | 91.7%         | 0.87                 |
| **Dark**       | 2            | 3.5 / 4                   | 87.5%         | 0.78                 |
| **Blurry**     | 2            | 2.5 / 4                   | 62.5%         | 0.60                 |

## 3. Preprocessing Impact & Recommendations
- **Auto-Rotation:** Handled efficiently by Gemini multimodal reasoning.
- **Low-Light Correction:** Improved via brightness normalization.
- **Blur Management:** Recommends OpenCV Laplacian variance filtering prior to API calls.
