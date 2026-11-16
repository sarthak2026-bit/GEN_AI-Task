# Test Execution Results (Day 3 Goal 2)

All 10 test queries were run against `agent.py` using Gemini function calling and the fake orders database.

| Test # | Category | Query Summary | Tools Called | Execution Order | Agent Response Summary | Status |
|---|---|---|---|---|---|---|
| **1** | Single-Tool | Details for order ORD-101 | `get_order` | 1. `get_order` | Provided order details for Aarav Sharma (Headphones, ₹12999, Delivered). | **PASS** |
| **2** | Single-Tool | Shipping status for ORD-102 | `get_shipping` | 1. `get_shipping` | Confirmed item is in-transit (Out for delivery in Mumbai). | **PASS** |
| **3** | Single-Tool | Refund policy for electronics | `check_refund_policy` | 1. `check_refund_policy` | Outlined 7-day return window and 10% restocking fee rules. | **PASS** |
| **4** | Multi-Tool | Items & shipping for ORD-107 | `get_order`, `get_shipping` | 1. `get_order`<br>2. `get_shipping` | Confirmed Mechanical Keyboard purchased and delivered via BlueDart. | **PASS** |
| **5** | Multi-Tool | Silk Saree return policy | `get_order`, `check_refund_policy` | 1. `get_order`<br>2. `check_refund_policy` | Verified order details (apparel category) and explained 15-day return policy. | **PASS** |
| **6** | Multi-Tool | Missing item dispute ORD-115 | `get_shipping`, `escalate_to_human` | 1. `get_shipping`<br>2. `escalate_to_human` | Checked delivery status and immediately triggered escalation due to non-receipt dispute. | **PASS** |
| **7** | Multi-Turn | Groceries policy -> Order ORD-105 | `check_refund_policy`, `get_order` | 1. `check_refund_policy`<br>2. `get_order` | Explained 24-hr grocery claim rule in turn 1, then successfully looked up tea pack in turn 2. | **PASS** |
| **8** | Multi-Turn | Order ORD-111 -> Shipping origin | `get_order`, `get_shipping` | 1. `get_order`<br>2. `get_shipping` | Retrieved Denim Jacket details in turn 1, then tracked dispatch source in turn 2. | **PASS** |
| **9** | Escalation | Cracked monitor ORD-104 (Angry) | `escalate_to_human` | 1. `escalate_to_human` | Detected angry sentiment and cracked screen dispute, escalated immediately. | **PASS** |
| **10** | Escalation | Manager request for ORD-108 | `escalate_to_human` | 1. `escalate_to_human` | Recognized explicit demand for human manager over delayed shipping and escalated. | **PASS** |

## Summary
- **Total Tests Run:** 10 / 10
- **Passed:** 10
- **Failed:** 0
- **Conclusion:** The customer service agent correctly selected single or multiple tools, handled multi-turn context seamlessly, and successfully enforced safety/dispute escalation protocols.
