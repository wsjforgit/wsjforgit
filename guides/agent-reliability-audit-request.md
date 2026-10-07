# Agent Reliability Audit — Request Template

Use this template to scope a review of one agent workflow.

## Workflow
- What outcome should the agent complete?
- Which tools or systems does it use?
- Which actions can create irreversible side effects?

## Current pain
Choose the closest:
- flaky completion;
- duplicate actions after retry;
- unclear permission boundary;
- weak recovery after disconnect;
- too many expensive model calls;
- hard-to-verify success;
- tool routing confusion.

## Evidence to include
- one representative run or log excerpt;
- current success/failure definition;
- known retry behavior;
- tool list;
- any existing eval set or benchmark.

## Desired output
Pick one:
- self-audit guidance;
- benchmark design;
- recovery/idempotency review;
- permissions/tool-boundary review;
- fixed-scope implementation audit.

This template is for demand discovery and scope clarification. It is not a promise of paid service availability.
