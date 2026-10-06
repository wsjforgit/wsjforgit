# Benchmark: Sometimes the Best AI Optimization Is Less AI

**Date:** 2026-10-07  
**System:** Laya → WebCodex routing stack

## Question

If WebCodex already exposes structured lifecycle metadata such as `status`, `exit_code`, and `command_execution_state`, should an AI classifier interpret that state first?

I compared:

1. a tiny deterministic status gate; and
2. the existing Laya route-only classifier.

No Codex upstream inference was started.

## Dataset

20 lifecycle snapshots selected from real WebCodex Job metadata:

- 10 successful completed jobs;
- 4 failed jobs;
- 6 timed-out jobs.

For this benchmark, timeouts are treated as `failed` because the workflow did not complete successfully.

The classifier target remained:

- `completed`
- `running`
- `failed`

## Deterministic rule

The prototype intentionally used simple rules:

- completed + execution completed + exit code 0 → `completed`
- failed / timeout / timed_out / non-zero exit → `failed`
- running / pending / queued with no exit code → `running`
- otherwise → fallback

The public prototype is available here:

- [deterministic_status_gate.py](../experiments/deterministic_status_gate.py)
- [edge-case tests](../experiments/test_deterministic_status_gate.py)

The nine published edge cases were executed after publication and **9/9 passed**.

## Results

| Metric | Deterministic gate | Laya route-only |
|---|---:|---:|
| Cases | 20 | 20 |
| Accuracy | **20/20 (100%)** | **14/20 (70%) raw** |
| Median decision time | **1.25 µs** | **103.64 ms router wall time** |
| Final local accepts at 0.90 threshold | 20/20 by deterministic rule | 0/20 |
| Upstream Codex calls started | 0 | 0 |

Mean raw Laya confidence was **0.4717**, well below the configured 0.90 local-accept threshold.

### Follow-up: live running snapshot

The original 20-case set had no live `running` job, so I launched a harmless local `sleep 30` WebCodex Job and captured its state while it was actually running:

- `status=running`
- `terminal=false`
- `activity_state=working`
- `activity_phase=process_running`
- no exit code yet

The deterministic rule classified it as `running`.

Laya also produced the correct raw decision, `running`, with confidence **0.6799**. Because that was below the configured **0.90** threshold, the live router still failed closed to the upstream path. The route-only test did not start Codex.

The sleep Job then completed normally with exit code 0.

## Interpretation

This is not a claim that deterministic logic is generally better than AI.

It is a narrower engineering rule:

> **When the system already has authoritative structured state, parse the state directly. Use AI for ambiguity, not for facts the runtime already knows.**

The AI router is more useful after deterministic evidence is exhausted.

A better hierarchy for this workflow is therefore:

1. **deterministic runtime evidence**
2. **local AI classifier for ambiguous natural-language state**
3. **strong upstream model for complex reasoning**
4. **human intervention when required**

## Why this matters for agent systems

Modern agents are not just models. They are harnesses that manage tools, state, permissions, recovery, and verification.

Routing everything through a model can add:

- unnecessary latency;
- additional calibration risk;
- avoidable inference cost;
- harder debugging.

A small deterministic layer can remove a whole class of unnecessary model decisions.

## Limits

- The 20-case benchmark used real Job lifecycle metadata, but the Laya classification prompt was standardized.
- The live-running observation was a separate follow-up sample rather than part of the original 20-case aggregate.
- This benchmark does not measure end-to-end product latency or token savings.
- The deterministic rule should still fail closed on unknown or conflicting states.

## Next step

Add a deterministic metadata gate in front of the local classifier **without changing the live production path yet**, then evaluate on:

- additional real running snapshots;
- conflicting state metadata;
- recovered jobs;
- server-restart reconciliation;
- partial/unknown execution state.

Only after that should the live routing policy change.

---

**Project:** Shengjie Builds AI  
**Theme:** agent reliability · routing · MCP · Codex · developer productivity
