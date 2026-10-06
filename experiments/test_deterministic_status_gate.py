from deterministic_status_gate import classify_job_state


def test_completed_requires_consistent_success_evidence():
    assert classify_job_state(
        status="completed", exit_code=0, command_execution_state="completed"
    ) == "completed"


def test_failed_status_wins():
    assert classify_job_state(
        status="failed", exit_code=1, command_execution_state="completed"
    ) == "failed"


def test_timeout_is_failed():
    assert classify_job_state(
        status="timeout", exit_code=-1, command_execution_state="timed_out"
    ) == "failed"


def test_running_without_exit_is_running():
    assert classify_job_state(
        status="running", exit_code=None, command_execution_state="running"
    ) == "running"


def test_pending_without_exit_is_running():
    assert classify_job_state(
        status="pending", exit_code=None, command_execution_state="pending"
    ) == "running"


def test_nonzero_exit_overrides_completed_label():
    assert classify_job_state(
        status="completed", exit_code=1, command_execution_state="completed"
    ) == "failed"


def test_completed_without_exit_evidence_fails_closed():
    assert classify_job_state(
        status="completed", exit_code=None, command_execution_state="completed"
    ) is None


def test_running_with_terminal_exit_fails_closed_to_failure():
    assert classify_job_state(
        status="running", exit_code=2, command_execution_state="completed"
    ) == "failed"


def test_unknown_state_fails_closed():
    assert classify_job_state(
        status="mystery", exit_code=None, command_execution_state="unknown"
    ) is None
