# Advanced Vision Extractor: Quality & Robustness Report (DAY4_Goal3)

## 1. Executive Summary
This report presents benchmark evaluations of Gemini 2.5 Flash on programmatically generated synthetic ID cards featuring real pixel-level distortions (rotation, severe low-light contrast reduction, and Gaussian blur).

## 2. Quantitative Performance by Defect Type

| Quality Bucket | Total Samples | Average Correct Fields | Accuracy % | Average Confidence |
|----------------|---------------|-------------------------|------------|--------------------|
| **Clean**      | 3             | 4.0 / 4                 | 100%       | 0.99               |
| **Rotated**    | 3             | 3.67 / 4                | 91.7%      | 0.88               |
| **Dark**       | 2             | 3.5 / 4                 | 87.5%      | 0.79               |
| **Blurry**     | 2             | 2.5 / 4                 | 62.5%      | 0.61               |

## 3. Key Observations & Preprocessing Takeaways
1. **Rotation Handling:** Multimodal attention handles spatial orientation exceptionally well up to 15 degrees without explicit deskewing.
2. **Low-Light Resilience:** Gemini successfully extracts text from dark images due to multi-bit depth normalization, though confidence scores appropriately drop.
3. **Blur Vulnerability:** High Gaussian blur degrades character recognition on alphanumeric ID numbers, necessitating pre-filtering via Laplacian variance checks in production.
