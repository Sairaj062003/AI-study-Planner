from models import StudyPlan, StudyItem
from harness.output_validator import validate_plan


def create_state(plan):

    return {
        "hours": 4,
        "subjects": "Python, DSA",
        "level": "Beginner",
        "priorities": [],
        "plan": plan,
        "evaluation": None,
        "feedback": "",
        "validation_status": "",
        "decision": "",
        "retry_reason": "",
        "error": None,
        "execution_trace": [],
        "attempt": 1
    }


def test_valid_plan():

    plan = StudyPlan(
        items=[
            StudyItem(
                subject="Python",
                hours=2.5,
                priority="High"
            ),
            StudyItem(
                subject="DSA",
                hours=1.0,
                priority="Medium"
            )
        ]
    )

    state = create_state(plan)

    result = validate_plan(state)

    assert result["validation_status"] == "VALID"

def test_plan_exceeds_available_time():

    plan = StudyPlan(
        items=[
            StudyItem(
                subject="Python",
                hours=3,
                priority="High"
            ),
            StudyItem(
                subject="DSA",
                hours=2,
                priority="Medium"
            )
        ]
    )

    state = create_state(plan)

    result = validate_plan(state)

    assert result["validation_status"] == "IMPROVE"    

def test_missing_subject():

    plan = StudyPlan(
        items=[
            StudyItem(
                subject="Python",
                hours=3,
                priority="High"
            )
        ]
    )

    state = create_state(plan)

    result = validate_plan(state)

    assert result["validation_status"] == "IMPROVE"

def test_unexpected_subject():

    plan = StudyPlan(
        items=[
            StudyItem(
                subject="Python",
                hours=2,
                priority="High"
            ),
            StudyItem(
                subject="DSA",
                hours=1,
                priority="Medium"
            ),
            StudyItem(
                subject="Java",
                hours=1,
                priority="Low"
            )
        ]
    )

    state = create_state(plan)

    result = validate_plan(state)

    assert result["validation_status"] == "IMPROVE"

def test_duplicate_subject():

    plan = StudyPlan(
        items=[
            StudyItem(
                subject="Python",
                hours=2,
                priority="High"
            ),
            StudyItem(
                subject="Python",
                hours=1,
                priority="Medium"
            ),
            StudyItem(
                subject="DSA",
                hours=1,
                priority="Medium"
            )
        ]
    )

    state = create_state(plan)

    result = validate_plan(state)

    assert result["validation_status"] == "IMPROVE"

def test_invalid_priority():

    plan = StudyPlan(
        items=[
            StudyItem(
                subject="Python",
                hours=2,
                priority="Urgent"
            ),
            StudyItem(
                subject="DSA",
                hours=1,
                priority="Medium"
            )
        ]
    )

    state = create_state(plan)

    result = validate_plan(state)

    assert result["validation_status"] == "IMPROVE"