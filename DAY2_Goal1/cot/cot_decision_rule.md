# Chain-of-Thought & Self-Consistency Decision Rule Report

## 1. Accuracy & Cost Performance Table

| Strategy | Accuracy (%) | Total Cost (USD) | Cost per Correct Answer (USD) |
| :--- | :--- | :--- | :--- |
| **Direct Prompting** | ~80.0% | $0.000035 | $0.00000291 |
| **Chain-of-Thought (CoT)** | ~93.3% | $0.000078 | $0.00000557 |
| **Self-Consistency (5x, Temp=0.7)**| **100.0%** | $0.000390 | $0.00002600 |

---

## 2. When to Use Which Technique? (Decision Rule)

* **Use Direct Prompting when:**
  - Tasks are straightforward, factual classification, or low-complexity extraction where reasoning overhead is unnecessary.
  - Speed and ultra-low cost are top priorities, and occasional minor logic slips are acceptable.

* **Use Chain-of-Thought (CoT) when:**
  - Tasks require multi-step logical deduction, arithmetic, or condition checking (e.g., matching complex insurance policy exclusions against claim clauses).
  - You want a significant accuracy boost (~10-15%) with only a minor increase in latency and token cost (~2x).

* **Use Self-Consistency when:**
  - Maximum reliability and rock-solid accuracy are mandatory (e.g., automated high-value financial payouts, legal compliance checks, edge-case medical/insurance triage).
  - You are willing to trade ~5x higher cost and latency to eliminate variance and hallucination risks via majority voting.
