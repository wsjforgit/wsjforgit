# Agent Reliability Checklist

A practical pre-production checklist for AI coding agents, MCP workflows, and long-running tool-using systems.

The goal is not to make the agent look autonomous. The goal is to make its behavior **observable, recoverable, and safe to trust**.

## 1. State: use the strongest evidence first

Before asking a model to infer state, check whether the runtime already knows it.

**Priority:**

1. authoritative structured runtime state;
2. deterministic rules;
3. local/cheap model for ambiguity;
4. stronger reasoning model;
5. human intervention.

Questions:

- [ ] Does the runtime expose `status`, `exit_code`, completion markers, or test results?
- [ ] Are conflicting states detected instead of silently resolved?
- [ ] Does unknown state fail closed?
- [ ] Can a completed claim be verified independently?

## 2. Tool selection

- [ ] Is every tool actually needed for the task?
- [ ] Can the agent distinguish read-only from write/destructive actions?
- [ ] Are tool schemas narrow enough to reduce accidental misuse?
- [ ] Is there a bounded fallback when a tool is unavailable?
- [ ] Are duplicate or overlapping tools removed from the active context?

## 3. Permission boundaries

- [ ] Are payments, credential changes, identity verification, and irreversible actions isolated?
- [ ] Does the agent know which actions require explicit authorization?
- [ ] Are secrets excluded from logs and model-visible output?
- [ ] Are third-party scopes minimized?

## 4. Checkpoints and resume

- [ ] Can a multi-step task resume from the last verified checkpoint?
- [ ] Is progress stored outside transient model context?
- [ ] Can the system distinguish “task failed” from “connection/stream failed”?
- [ ] Does retry continue the same operation rather than accidentally duplicating it?

## 5. Idempotency

- [ ] Can repeated tool calls create duplicate records, posts, payments, or deployments?
- [ ] Are write operations protected by identifiers, revisions, or expected state?
- [ ] Are retries safe after timeouts or unknown outcomes?

## 6. Verification

- [ ] Is tool success verified at the business-outcome level?
- [ ] Does “HTTP 200” or “tool completed” get treated separately from “task succeeded”?
- [ ] Are critical outputs re-read after writes?
- [ ] Are tests or assertions tied to the intended outcome?

## 7. Fallback behavior

- [ ] Is there a confidence threshold?
- [ ] Is the threshold calibrated on representative data?
- [ ] Does low confidence trigger escalation rather than guessing?
- [ ] Are completion claims held to a higher evidence standard?

## 8. Observability

Log at least:

- task / workflow ID;
- decision path;
- tool chosen;
- confidence where applicable;
- latency;
- retry count;
- human interventions;
- upstream model calls;
- token/cost data when available;
- final verified outcome.

## 9. Recovery

- [ ] Can the system detect process/server restarts?
- [ ] Can it reconcile jobs after reconnect?
- [ ] Are lost/unknown outcomes surfaced explicitly?
- [ ] Does recovery avoid replaying destructive steps?

## 10. Cost and latency

Do not optimize based on intuition.

Measure separately:

- local routing latency;
- upstream model latency;
- tool/network latency;
- cached vs uncached tokens;
- calls avoided;
- retries added;
- human time saved.

A cheaper model that causes more retries can be more expensive overall.

## 11. Evaluation set

Your eval should include:

- clear successful cases;
- clear failures;
- running/in-progress states;
- ambiguous cases;
- conflicting evidence;
- timeouts;
- partial completion;
- stale state;
- adversarial or misleading completion claims.

## 12. Go / No-Go rule

Do not promote an optimization to production because it “usually works.”

Require explicit thresholds for:

- false-local-accept rate;
- task success rate;
- regression rate;
- latency;
- cost;
- human intervention rate.

If the optimization cannot beat the existing system on the metric it claims to improve, keep it experimental.

---

## Quick score

Score each section:

- **0** = missing
- **1** = partially implemented
- **2** = measured and verified

Maximum score: **24**

Suggested interpretation:

- **0–8:** demo-grade
- **9–16:** usable with active supervision
- **17–21:** production-oriented
- **22–24:** mature baseline; continue adversarial testing

The score is a prioritization aid, not a certification.

---

## Core principle

> **Use deterministic facts first. Use AI for ambiguity. Use stronger AI for reasoning. Use humans for authority.**

This checklist is based on hands-on experiments with AI coding-agent routing, tool orchestration, recovery, and verification.

**Shengjie Builds AI**  
AI Coding Agents · MCP · Codex · Agent Reliability · Developer Productivity
