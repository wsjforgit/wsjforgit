# G02 — Confidence Threshold Calibration

Sample: 20 previously measured WebCodex job-state snapshots.
Raw local-model accuracy: 70.0%.

| Threshold | Coverage | Accepted accuracy | False accepts |
|---:|---:|---:|---:|
| 0.00 | 100.0% | 70.0% | 6 |
| 0.40 | 95.0% | 73.7% | 5 |
| 0.45 | 60.0% | 100.0% | 0 |
| 0.50 | 45.0% | 100.0% | 0 |
| 0.55 | 0.0% | n/a | 0 |
| 0.60 | 0.0% | n/a | 0 |
| 0.70 | 0.0% | n/a | 0 |
| 0.80 | 0.0% | n/a | 0 |
| 0.90 | 0.0% | n/a | 0 |

## Decision
threshold qualifies.

Confidence is a routing signal, not proof of correctness. This result is post-hoc and narrow; it does not establish production calibration.