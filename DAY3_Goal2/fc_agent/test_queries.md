# Test Queries for Customer Service Agent (Day 3 Goal 2)

The 10 test queries are categorized into single-tool usage, multi-tool workflows, multi-turn conversations, and escalation scenarios.

## Category A: Single-Tool Queries (3)
1. **Order Lookup:** "Can you tell me the details for order ORD-101?" -> Expected: `get_order`
2. **Shipping Status:** "Where is my order ORD-102 right now?" -> Expected: `get_shipping`
3. **Refund Policy:** "What is your refund policy for electronics?" -> Expected: `check_refund_policy`

## Category B: Multi-Tool Queries (3)
4. **Order + Shipping Check:** "What items did I buy in order ORD-107 and has it been delivered?" -> Expected: `get_order` + `get_shipping`
5. **Order + Policy Check:** "I bought a Silk Saree (ORD-108). Can I return it if I don't like it?" -> Expected: `get_order` + `check_refund_policy`
6. **Shipping + Escalation check:** "Check shipping for ORD-115, it says delivered but I never received anything!" -> Expected: `get_shipping` + `escalate_to_human`

## Category C: Multi-Turn Conversations (2)
7. **Turn 1 (Policy) -> Turn 2 (Order):** 
   - Turn 1: "What is the policy for groceries?" (`check_refund_policy`)
   - Turn 2: "Okay, check details for order ORD-105." (`get_order`)
8. **Turn 1 (Order Status) -> Turn 2 (Shipping Tracking):**
   - Turn 1: "Look up order ORD-111." (`get_order`)
   - Turn 2: "Where is it currently shipped from?" (`get_shipping`)

## Category D: Escalation Triggers (2)
9. **Angry Customer / Dispute:** "This is ridiculous! My monitor (ORD-104) arrived with a cracked screen. I want my money back right now or I am filing a complaint!" -> Expected: `escalate_to_human`
10. **Explicit Human Request:** "I am extremely frustrated with this delayed delivery for ORD-108. Connect me to a human manager immediately!" -> Expected: `escalate_to_human`
