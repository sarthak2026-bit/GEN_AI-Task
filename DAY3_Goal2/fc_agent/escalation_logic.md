# Escalation Logic & Protocol (Day 3 Goal 2)

## What Triggers Escalation?
The agent automatically calls the `escalate_to_human` tool under the following conditions:
1. **Disputed Deliveries:** Orders marked as delivered where the customer reports missing items, stolen packages, or damaged/cracked goods (e.g., ORD-104, ORD-115).
2. **Customer Sentiment & Tone:** Aggressive language, anger, threats of legal/consumer complaints, or extreme frustration.
3. **Explicit Requests:** Direct demands to speak with a human manager, supervisor, or customer care executive.
4. **System/Process Failures:** Orders stuck in processing or anomalous tracking states that cannot be resolved via standard automated lookups.

## What Context is Passed During Escalation?
When `escalate_to_human` is invoked, the agent passes:
- **`reason`:** A synthesized summary of the customer's grievance, order ID (if applicable), and emotional tone/urgency level.
- **System Action:** Logs the escalation status, provides a support ticket assurance, and commits to a callback window (2-4 business hours) for a senior supervisor.
