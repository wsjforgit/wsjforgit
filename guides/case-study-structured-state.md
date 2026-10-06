# Case Study — Structured State Before AI

## Problem
A coding-agent workflow was asking a local model to interpret job state even though the runtime already exposed authoritative structured metadata.

## Experiment
20 real WebCodex Job lifecycle snapshots were evaluated.

## Result
- Deterministic state rule: 20/20 correct.
- Local model raw accuracy: 14/20.
- Deterministic median decision time: 1.25 microseconds.
- Local router median wall time: 103.64 ms.
- Upstream Codex calls started: 0.

## Engineering change
Prefer:
1. authoritative runtime facts;
2. deterministic checks;
3. local model for ambiguity;
4. stronger model for complex reasoning;
5. human authority for protected actions.

## Scope
This is a narrow state-classification result, not a general rules-vs-AI claim.