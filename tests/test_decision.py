from models import PlanEvaluation
from nodes.decision import decide_from_evaluation


def test_good_evaluation_is_accepted():

    evaluation = PlanEvaluation(
        time_fit_score=9,
        subject_coverage_score=9,
        priority_alignment_score=8,
        level_suitability_score=9,
        realism_score=8,
        overall_feedback="Good plan."
    )

    decision, reason = decide_from_evaluation(
        evaluation
    )

    assert decision == "ACCEPT"
    assert reason == ""


def test_bad_evaluation_requires_retry():

    evaluation = PlanEvaluation(
        time_fit_score=5,
        subject_coverage_score=9,
        priority_alignment_score=6,
        level_suitability_score=8,
        realism_score=5,
        overall_feedback="Needs improvement."
    )

    decision, reason = decide_from_evaluation(
        evaluation
    )

    assert decision == "RETRY"
    assert reason != ""