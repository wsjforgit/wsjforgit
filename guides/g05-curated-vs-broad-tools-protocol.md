# G05 — Curated vs Broad MCP Tool Set

## Question
Does exposing a smaller, task-relevant tool set improve verified task success or reduce routing overhead compared with a broad tool set?

## Hypothesis
A curated tool set will reduce unnecessary tool-selection attempts and latency without reducing verified task success.

## Design
Use the same representative task set in two frozen conditions.

### A — Broad
Expose the normal broad MCP tool catalog available to the workflow.

### B — Curated
Expose only tools required for the task family plus one explicit fallback path.

Do not change prompts, model version, task inputs, success criteria, or external data between A and B.

## Required task set
Include at least:
- straightforward read-only retrieval;
- one multi-step read workflow;
- one safe write with verification;
- one transient tool failure;
- one ambiguous routing case;
- one case where no tool should be called.

## Primary metric
Verified task success rate.

## Secondary metrics
- tool calls per completed task;
- wrong-tool selections;
- retries;
- median wall time;
- model/tool-routing tokens if available;
- human interventions.

## Safety metric
No increase in incorrect or irreversible side effects.

## Evidence rule
A tool invocation returning success is not sufficient. Verify the intended business outcome separately.

## Decision
Prefer curated exposure only if verified task success is non-inferior and at least one routing-efficiency metric improves without a safety regression.

## Limitation
This protocol tests tool-surface design for the selected task family; it does not claim that fewer tools are universally better.
