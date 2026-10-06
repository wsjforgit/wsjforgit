# Laya → WebCodex Router Benchmark — 2026-10-07

## Question

Can a local pre-router safely handle simple workflow-status classification and reduce unnecessary upstream model calls?

This benchmark evaluates **routing behavior only**. It does not measure real token savings, dollar savings, or end-to-end task productivity.

## Setup

- Local router: Laya → WebCodex
- Laya version: **0.3.28**
- Device: **Apple MPS**
- Local accept threshold: **0.90 confidence**
- Mode: **route-only**
- Upstream Codex execution: **disabled**
- Cases: **40 synthetic prompts**

The 40 prompts contained:

- 30 explicit status-classification cases
  - 10 expected `running`
  - 10 expected `failed`
  - 10 expected `completed` with completion evidence
- 5 adversarial completion cases
- 5 non-status tasks that should be rejected by the outer gate

## Results

| Metric | Result |
|---|---:|
| Total cases | 40 |
| Outer-gate eligible | 35 |
| Raw Laya answers | 35 |
| Raw status-classification accuracy | **18/30 (60%)** |
| Mean raw Laya confidence | **0.4879** |
| Final local accepts at threshold 0.90 | **0/40** |
| Low-confidence fallbacks | **35** |
| Non-status cases rejected before local inference | **5/5** |
| Unsafe completion accepts | **0** |
| Codex calls actually started | **0** |
| Median router-reported wall time | **98.82 ms** |

### Per-class raw accuracy

| Expected class | Correct | Total |
|---|---:|---:|
| running | 6 | 10 |
| failed | 5 | 10 |
| completed | 7 | 10 |

The highest observed raw confidence in the benchmark was **0.7208**, still below the configured local-accept threshold of **0.90**.

## What this does mean

The current configuration is **fail-safe and conservative** on this synthetic benchmark:

- non-status work was not accidentally routed into the local status classifier;
- no low-confidence local answer was allowed to take over;
- no unsafe completion claim was locally accepted;
- the configured threshold prevented questionable raw predictions from becoming final routing decisions.

## What this does *not* mean

It does **not** prove:

- a 0% long-term local-handling rate;
- a specific percentage of token savings;
- a specific dollar saving;
- production accuracy on real workflow logs;
- that Laya is generally good or bad.

Earlier mixed operational logs contained a small number of high-confidence local accepts, so the next experiment should use **real, labeled workflow-state examples** rather than only synthetic prompts.

## Next experiment

Build a labeled dataset from real WebCodex task-state observations, then measure:

1. raw classification accuracy;
2. calibration / confidence distribution;
3. false-local-accept rate;
4. fallback rate;
5. latency;
6. actual upstream calls avoided;
7. token and cost savings only after paired measurement.

## Reproducibility note

The benchmark intentionally used a route-only mode so that no Codex upstream inference was started during the test. The purpose was to isolate the router's behavior rather than generate an impressive savings number.

---

**Project:** Shengjie Builds AI  
**Topic:** AI coding agents · MCP · Codex · routing · reliability
