# Example Agent Reliability Audit Report

Synthetic example only. This is not a customer result.

## Score output

TOTAL=36/48
MATURITY=production-oriented
SECTION State=7/8
SECTION Tools=5/8
SECTION Permissions=6/6
SECTION Checkpoints=4/6
SECTION Idempotency=1/2
SECTION Verification=4/4
SECTION Fallback=4/6
SECTION Observability=2/2
SECTION Recovery=1/2
SECTION Evaluation=1/2
SECTION Economics=1/2

## Example top risks
1. Incomplete checkpoint/recovery design.
2. Threshold calibration is not yet supported by representative eval data.
3. Cost savings are assumed rather than measured.

## Example first experiment
Introduce a deterministic runtime-state gate before model inference.

Measure false terminal-state accepts, upstream model calls, median decision latency, retries, and verified task success.

## Example decision rule
Ship only if verified task success does not regress and false local accepts remain below the agreed threshold.
