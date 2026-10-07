# Agent Reliability Audit — Intake Interview

Use before scoring a workflow.

## Workflow
1. What user/business outcome is the agent supposed to complete?
2. What are the start and terminal states?
3. What external systems does it touch?
4. What actions can create irreversible side effects?

## Runtime state
5. Which facts are already known structurally by the runtime?
6. Which decisions are still inferred from natural language?
7. How is “completed” verified?
8. What happens when state is missing or contradictory?

## Tools
9. How many tools are exposed at once?
10. Which are read-only, write, destructive, or financial?
11. Are there overlapping tools that solve the same problem?
12. What is the fallback when the preferred tool fails?

## Permissions
13. Which actions can the agent take without asking?
14. Which actions require user approval?
15. Are credentials, tokens, or PII visible to the model?

## Long-running behavior
16. How are checkpoints stored?
17. What happens after a stream/browser/server disconnect?
18. Can the same write be replayed accidentally after a timeout?
19. Can the workflow resume without redoing already-completed steps?

## Verification
20. What evidence proves the business outcome actually happened?
21. Are writes re-read?
22. Are test/build/deploy results distinguished from command success?

## Evaluation
23. What representative eval set exists?
24. What false-accept/fallback/intervention rates are acceptable?
25. Which metric is the optimization actually trying to improve?
26. How is cost measured?

## Commercial/operational constraints
27. Which external platform rules constrain automation?
28. Which steps must remain human-authorized?
29. What is the cost of one failed/duplicated action?
30. What is the cost of one unnecessary strong-model call?
