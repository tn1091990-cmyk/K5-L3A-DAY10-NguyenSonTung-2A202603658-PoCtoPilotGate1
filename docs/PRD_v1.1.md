# LogiX-VN evaluation requirements v1.1

## Purpose

Before an agent change is merged, replay a fixed, versioned set of claims across deterministic seeds, grade outcomes and safety from independent labels and ledger traces, and block material regressions. No API key is required for this lab: the harness uses MockLLM and replayed judge decisions.

## Requirements

1. Keep eval inputs and expected labels separate. Every item carries a stable ID, source/matrix provenance, split, version, and one or more failure-mode tags.
2. Score a run on item × seed cases. Use deterministic code graders for secrets, ownership, approval, refund amount, DB facts, and reply-to-ledger consistency.
3. Calibrate qualitative judges against human labels; report confusion matrix, precision, recall, Cohen κ, and Rogan–Gladen adjusted failure prevalence. A judge failing its floors cannot be a merge gate.
4. Compare paired per-item results with a seeded percentile bootstrap. Block below-floor capability and safety violations without averaging them away.
5. Preserve baseline provenance, row completeness, item/seed identities, slice tags, evaluator health, and monotonic thresholds. A malformed or manipulated report fails closed.
6. Keep Day 8 `lab8/` unchanged; Day 9 reads its reference shape and replays changes from an overlay.

## v1 acceptance

- 14 public cases × five seeds, labels separated, all failure tags mapped to the taxonomy.
- Tone judge meets κ≥0.6, precision≥0.8, recall≥0.7; helpfulness judge fails and is excluded from gating.
- `fixed` merges; `seeded_regression` is blocked on `pass_rate` (observed Δ −0.271; paired 95% CI [−0.500, −0.057]).
- Report has a run ID and states the limitations: deterministic MockLLM, 14 claims, five seeds, public data, and replayed judges.

## v2 extension

Include adversarial cases and tags for `money_movement` and `adversarial`; require ≥3 items for every attacked FM. Gate slices, `pass_hat_5`, reply/ledger mismatch, and evaluation integrity. Thresholds are chosen outside the A/A noise band. Five seeds cannot reliably detect an error that occurs on only one of three trials; add seeds or targeted cases for that risk.
