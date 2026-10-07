# Agent Reliability Audit Kit — Free Beta

A small, evidence-oriented toolkit for reviewing AI coding agents, MCP workflows, and long-running tool-using systems.

## Included
- audit_scorecard.csv — 24 checks, maximum 48 points.
- audit_interview.md — workflow intake questions.
- audit_report_template.md — structured audit deliverable.
- experiment_template.md — before/after evaluation template.
- score_audit.py — local score calculator.
- delivery_guide.md — self-audit/team-review workflow.
- sample_audit_report.md — synthetic example only.
- case_study_structured_state.md — measured narrow case study.

## Use

1. Fill every score in audit_scorecard.csv with 0, 1, or 2.
2. Add concrete evidence for each score.
3. Run: python3 score_audit.py audit_scorecard.csv
4. Treat every 0/1 as a gap to investigate.
5. Pick at most three P0 changes for the first iteration.
6. Verify improvement with an explicit experiment, not intuition.

## Boundaries

- This free beta is not a certification.
- The sample report is synthetic.
- Do not include credentials, customer secrets, or private data in public issues.
- Measured Project X1M benchmark results are narrow examples, not universal production claims.
- No paid-service availability or pricing is promised by this kit.
