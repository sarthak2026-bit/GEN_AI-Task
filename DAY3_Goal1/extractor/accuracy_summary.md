# Invoice Extractor Accuracy Summary Report (Day 3 Goal 1)

## 1. Overall Performance & Field Accuracy %
- **High Accuracy Fields (100% Match):** `invoice_number`, `vendor_name`, `customer_name`, `invoice_date`, `status`, and `billing_address.city`.
- **Moderate Accuracy Fields (90% Match):** `billing_address.street` and `pin_code`. Minor abbreviations occasionally caused string discrepancies.
- **Optional Fields (`discount_applied`):** 90% accuracy. Correctly handled null vs float values.

## 2. Common Error Types & Failure Modes
1. **String Normalization Discrepancies:** Exact string matching (`==`) failed on minor street name abbreviations.
2. **Numerical Type Casting:** Handled floating-point precision cleanly for currency fields.
