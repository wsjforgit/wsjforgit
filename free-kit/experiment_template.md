# Agent Workflow Experiment Template

## Hypothesis
Example:
“Adding a deterministic runtime-state gate before the local model reduces unnecessary model decisions without increasing false terminal-state accepts.”

## Unit of analysis
One task / workflow / tool decision / job state.

## Baseline
Describe current behavior and freeze:
- code revision;
- model/version;
- tool set;
- threshold;
- test set;
- environment.

## Treatment
Exactly one main change.

## Metrics
Primary:
- verified task success rate.

Safety:
- false local accept rate;
- incorrect terminal-state rate;
- duplicate side effects.

Efficiency:
- upstream model calls;
- input/output tokens;
- latency;
- retries;
- human interventions;
- cost.

## Test set
Include:
- success;
- failure;
- running;
- timeout;
- ambiguous;
- conflicting evidence;
- stale state;
- recovered state.

## Stop conditions
Stop/revert if:
- false local accepts exceed threshold;
- business outcome regressions appear;
- irreversible duplicate actions occur;
- measurement integrity is lost.

## Result
- Baseline:
- Treatment:
- Difference:
- Confidence/uncertainty:
- Unexpected failures:

## Decision
- Ship
- Iterate
- Reject
- Need more evidence
