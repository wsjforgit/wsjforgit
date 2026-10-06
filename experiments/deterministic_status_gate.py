"""Minimal deterministic WebCodex-style job-state gate.

Use authoritative runtime metadata before asking a model to infer state.
Unknown or conflicting states fail closed by returning None.
"""

from __future__ import annotations
from typing import Literal

JobState = Literal["completed", "running", "failed"]


def classify_job_state(
    *,
    status: str | None,
    exit_code: int | None,
    command_execution_state: str | None,
) -> JobState | None:
    status = (status or "").strip().lower()
    execution = (command_execution_state or "").strip().lower()

    # Explicit unsuccessful terminal states win.
    if status in {"failed", "timeout"}:
        return "failed"
    if execution in {"failed", "timed_out"}:
        return "failed"
    if exit_code is not None and exit_code != 0:
        return "failed"

    # Success requires mutually consistent terminal evidence.
    if status == "completed" and execution == "completed" and exit_code == 0:
        return "completed"

    # Running/pending work must not already have a terminal exit code.
    if status in {"running", "pending", "queued"} and exit_code is None:
        return "running"

    # Conflicting or unknown state: let the next layer decide.
    return None
