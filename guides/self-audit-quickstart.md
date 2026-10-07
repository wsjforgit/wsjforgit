# 10-Minute Agent Reliability Self-Audit

Use this when an agent workflow works in demos but you are unsure whether it is safe or reliable enough to trust.

## Minute 0–2 — State
- What does the runtime know directly?
- Does completion require independent evidence?
- Does unknown or conflicting state fail closed?

## Minute 2–4 — Tools and authority
- Which tools can write, publish, delete, pay, or change credentials?
- Which actions require human authority?
- Are overlapping tools increasing routing ambiguity?

## Minute 4–6 — Recovery
- Is progress checkpointed outside model context?
- Can a timeout replay an already-completed write?
- Can the workflow distinguish connection failure from task failure?

## Minute 6–8 — Verification
- Does tool success equal business success? Usually not.
- Are important writes re-read or reconciled?
- Are tests, receipts, IDs, or external state used as proof?

## Minute 8–10 — Measurement
Record:
- verified task success;
- false local accepts;
- retries;
- upstream model calls;
- tool calls;
- latency;
- human interventions;
- cost only when actually measured.

## Decision

If you cannot answer the state, authority, recovery, and verification questions with evidence, treat the workflow as supervised rather than autonomous.

For a fuller review, use the [Agent Reliability Checklist](agent-reliability-checklist.md) and [Audit Request Template](agent-reliability-audit-request.md).
