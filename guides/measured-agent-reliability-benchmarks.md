# Measured Agent Reliability Benchmarks

| Evidence | Scope | Key result |
|---|---|---|
| Structured job state | 20 real WebCodex job-state snapshots | deterministic rule 20/20; local model raw accuracy 14/20 |
| G02 confidence calibration | post-hoc threshold sweep on the same 20 snapshots | threshold acceptance calibrated against explicit accuracy and coverage gates |
| G06 recovery harness | 24 controlled paired trials | checkpointed 24/24; one-shot 4/24 under the constructed interruption model |
| G07 verification harness | 24 adversarial constructed cases | verification caught 16 hidden failures despite 24/24 operation-level success |

## Interpretation
Controlled/adversarial case ratios are not production prevalence estimates. Tool success is not business success. Confidence is a routing signal, not proof.
