from models import PlanEvaluation
from trace import create_execution_trace


def test_execution_trace_records_evaluation():

    evaluation = PlanEvaluation(
        time_fit_score=8,
        subject_coverage_score=9,
        priority_alignment_score=7,
        level_suitability_score=9,
        realism_score=8,
        memory_consistency_score=8,
        overall_feedback="Good plan."
    )

    trace = create_execution_trace(
        attempt=1,
        validation_status="VALID",
        evaluation=evaluation,
        decision="ACCEPT",
        reason="",
        error=None
    )

    assert trace.attempt == 1
    assert trace.validation_status == "VALID"
    assert trace.time_fit_score == 8
    assert trace.subject_coverage_score == 9
    assert trace.priority_alignment_score == 7
    assert trace.memory_consistency_score == 8
    assert trace.decision == "ACCEPT"