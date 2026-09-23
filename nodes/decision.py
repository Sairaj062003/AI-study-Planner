from trace import create_execution_trace
from decision import decide_next_action, decide_from_evaluation
from state import StudyState


def decision_engine(state: StudyState):
    """
    Decide whether the workflow should accept,
    retry, or fail.
    """
    
    decision, reason = decide_next_action(
        state
    )

    print(
        f"Decision engine: {decision}"
    )

    if reason:

        print(
            f"Reason: {reason}"
        )

    trace_entry = create_execution_trace(
        attempt=state["attempt"],
        validation_status=state["validation_status"],
        evaluation=state["evaluation"],
        decision=decision,
        reason=reason,
        error=state["error"]
    )
    

    updated_trace = (
        state["execution_trace"]
        + [trace_entry]
    )


    if decision == "RETRY":

        print(
            "The plan needs improvement. "
            "Regenerating..."
        )


    elif decision == "ACCEPT":

        print(
            "The plan passed the evaluation."
        )


    elif decision == "FAIL":

        print(
            "Workflow failed."
        )


    return {
        "decision": decision,
        "retry_reason": reason,
        "execution_trace": updated_trace
    }