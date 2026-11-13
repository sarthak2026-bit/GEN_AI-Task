# Prompt Styles Evaluation Findings

## Accuracy Table
| Prompt Style | Correct Predictions | Total Tickets | Accuracy (%) |
| :--- | :---: | :---: | :---: |
| Zero-Shot | 29 / 30 | 30 | 96.67% |
| Few-Shot | 29 / 30 | 30 | 96.67% |
| Role-Based | 28 / 30 | 30 | 93.33% |

## Examples Where Styles Won
1. **Zero-Shot:** Handled direct, straightforward category requests effectively without extra tokens.
2. **Few-Shot:** Provided examples clearly separated tricky categories like *Payment* vs *Refund*.
3. **Role-Based:** The expert persona accurately captured nuanced intent in customer complaints.

## Examples Where Styles Failed
1. **Zero-Shot:** Lacked constraints on boundary categories like *Shipping* and *Order Change*.
2. **Few-Shot:** Over-relied on provided examples for completely unique queries.
3. **Role-Based:** Occasionally over-analyzed simple queries, adding minor overhead.

## Conclusion: When to Use Which Style
* **Zero-Shot:** Best for quick, simple classification tasks.
* **Few-Shot:** Best when strict formatting and clear multi-class boundaries are needed.
* **Role-Based:** Best for complex, domain-specific intent analysis.