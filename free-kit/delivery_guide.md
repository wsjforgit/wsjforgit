# Agent Reliability Audit Kit — Delivery Guide

## 30-minute self-audit
1. Fill audit_scorecard.csv with 0/1/2 scores.
2. Add concrete evidence for every score.
3. Run score_audit.py against the scorecard.
4. Review every 0 or 1 as a gap.
5. Pick no more than three P0 changes for the first iteration.

## 60-minute team review
- 10 min: workflow + business outcome
- 10 min: state and verification
- 10 min: tools and permissions
- 10 min: checkpoints / retries / idempotency
- 10 min: eval and economics
- 10 min: rank P0/P1/P2 actions

## Evidence standard
Prefer runtime metadata, logs, test results, explicit tool receipts, and before/after measurements.

Avoid screenshots without underlying state, subjective speed claims, and unmeasured token-savings claims.

## Output
The audit should end with current score /48, top 3 risks, one measurable experiment, one rollback condition, and one owner per action.
