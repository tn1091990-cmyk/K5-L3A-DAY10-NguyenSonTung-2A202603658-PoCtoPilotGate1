# Evaluation card — LogiX-VN

## v1 core

- Dataset: 14 public claims, five seeds (11, 22, 33, 44, 55); labels stored separately. Source: Day 8 public claim matrix. Eval set SHA-12: `f9e56627e353`.
- Baseline: `E-swarm-20261117-f9e5`; MockLLM. Pass rate 0.9857 (69/70); safety counts: approval bypass 0, secret leak 0. Refund and proposal amount correctness 0.9857; DB fact kept 0.9857.
- `fixed`: pass rate 1.0000; gate exit 0. `seeded_regression`: pass rate 0.7143 (50/70), Δ −0.271; paired 95% bootstrap CI [−0.500, −0.057]; gate exit 1, including `pass_rate`.
- Tone judge: precision .857, recall .800, κ .757; Rogan–Gladen fail prevalence .300 versus observed .280. Usable as qualitative monitored signal. Helpful judge: precision 1.000, recall .300, κ .375; not eligible to gate.
- Limitations: deterministic MockLLM, 14 claims, five seeds, public cases and replayed judge labels. These results do not estimate production model drift or rare-event rates.

## v2 advanced / expert

- Dataset: v1 plus 14 adversarial items, 28 total × five seeds; labels separate. Every attacked failure mode occurs in at least three items. Eval set SHA-12: `5043b804b97c`.
- Baseline: `E-swarm-20261117-5043`; pass rate .9786, `pass_hat_5` .8929, approval bypass 0, secret leak 0. A/A seeds 66,77,88,99,110 produced Δ=0 for every reported metric in MockLLM. Use floors outside observed noise; `pass_hat_5` blocking floor is .80.
- Blocking slices: `money_movement` and `adversarial` plus denial regression check. `slice_regression` retained overall pass .9357 and paired CI [−.121, +.029], which touches zero; money movement averaged .85 against a .90 floor (slice CI [−.300, 0.000]), so the slice gate blocks it.
- Mutation scorecard: fixed and honest_refactor merge; seeded_regression, slice_regression and flaky_regression block. Score 3/3, false alarms 0. Public integrity traps `evaluator_errors_as_nan`, `dropped_failing_rows`, `cherry_picked_seeds`, and `loosened_spec` all block.
- Sample limit: with five seeds, a defect that appears on only one of three runs is not detected reliably. Add targeted cases or more seeds when that risk matters.

Reports are script-generated under `src/reports/`; do not edit their metrics by hand. Run IDs and JSON artifacts are the source of truth if a replay changes.
