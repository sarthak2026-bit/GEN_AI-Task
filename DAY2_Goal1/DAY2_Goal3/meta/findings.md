# Meta-Prompting Findings: When to Use vs. Manual Prompting

## 1. When Meta-Prompting Helps (High Value)
- **Cold-Start Problem:** When building a brand-new workflow or feature for a client where you don't know the optimal prompt structure, a meta-prompt quickly generates a comprehensive 6-part baseline.
- **Standardization:** Enforces uniform prompt hygiene (Role, Context, Task, Constraints, Format, Examples) across team members or automated pipeline generators.
- **Complex Domain Expansion:** Quickly bootstrapping prompts for unfamiliar domains (e.g., legal or medical compliance) where expert personas and edge-case constraints are hard to recall manually.

## 2. When Manual Prompting is Faster (Low Overhead)
- **Iterative Tweaking & Fine-Tuning:** When you are already in the middle of debugging a prompt and need to adjust a single constraint or example, running a meta-prompt adds unnecessary round-trips.
- **Hyper-Specific Constraints:** For simple, highly deterministic tasks (e.g., regex extraction or basic formatting), writing a direct 3-line prompt manually is faster and gives you absolute control over every token.
- **Low-Latency Prototyping:** When experimenting locally where speed and immediate feedback loop take precedence over formal structural completeness.
