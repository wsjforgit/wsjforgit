# Shengjie Builds AI

Software engineer and AI researcher building and testing **AI coding agents** with measured evidence.

I focus on:
- **Codex / agentic software engineering**
- **MCP and tool orchestration**
- **Agent reliability, routing, recovery, and verification**
- **Developer productivity experiments**

## Start here

- [Resource Hub](guides/resource-hub.md)
- [Agent Reliability Checklist](guides/agent-reliability-checklist.md)
- [10-minute Self-Audit](guides/self-audit-quickstart.md)
- [Measured Benchmark Index](guides/measured-agent-reliability-benchmarks.md)

## Latest measured finding

### Sometimes the best AI optimization is less AI

On 20 real WebCodex Job lifecycle metadata snapshots:
- deterministic state rule: **20/20**
- local model raw classification: **14/20**
- deterministic median decision time: **1.25 µs**
- local router median wall time: **103.64 ms**
- upstream Codex calls started in the route-only test: **0**

The narrow engineering lesson:

> When authoritative structured state already exists, parse it directly. Use AI for ambiguity, not for facts the runtime already knows.

See [Structured State Before AI](guides/case-study-structured-state.md).

## Current public experiments

- [G02 — Confidence Threshold Calibration](guides/g02-confidence-threshold-calibration.md)
- [G05 — Curated vs Broad MCP Tool Set Protocol](guides/g05-curated-vs-broad-tools-protocol.md)
- [Agent Reliability Maturity Matrix](guides/agent-reliability-maturity-matrix.md)
- [Demand Qualification Rubric](guides/demand-qualification-rubric.md)

## How I work

I publish negative results, failure autopsies, explicit limitations, and reproducible experiments where possible.

I do **not** claim token, latency, cost, or business impact without measurement.

---

**AI Coding Agents · MCP · Codex · Agent Reliability · Developer Productivity**
