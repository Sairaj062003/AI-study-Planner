from models import (
    ExecutionTrace,
    PlanEvaluation,
    WorkflowError
)


def create_execution_trace(
    attempt: int,
    validation_status: str,
    evaluation: PlanEvaluation | None,
    decision: str,
    reason: str,
    error: WorkflowError | None
):

    error_type = None
    error_message = None


    if error is not None:

        error_type = error.error_type
        error_message = error.message


    if evaluation is None:

        return ExecutionTrace(
            attempt=attempt,
            validation_status=validation_status,
            decision=decision,
            reason=reason,
            error_type=error_type,
            error_message=error_message
        )


    return ExecutionTrace(
        attempt=attempt,
        validation_status=validation_status,

        time_fit_score=(
            evaluation.time_fit_score
        ),

        subject_coverage_score=(
            evaluation.subject_coverage_score
        ),

        priority_alignment_score=(
            evaluation.priority_alignment_score
        ),

        level_suitability_score=(
            evaluation.level_suitability_score
        ),
        realism_score=(
            evaluation.realism_score
        ),
        memory_consistency_score=(
            evaluation.memory_consistency_score
        ),

        decision=decision,
        reason=reason,

        error_type=error_type,
        error_message=error_message
    )