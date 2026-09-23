from state import StudyState

from models import SessionFeedback

from harness.session_validator import (
    validate_session_feedback
)

from memory.session_memory import (
    create_session_memory
)


def collect_session_feedback(
    state: StudyState
):
    """
    Collect the user's actual study result.
    Shows the plan first so the user knows what to report.
    """

    # ------------------------------------------
    # Show the study plan before asking feedback
    # ------------------------------------------

    plan = state["plan"]

    print(
        "\n========== YOUR STUDY PLAN =========="
    )

    total_hours = 0

    for index, item in enumerate(
        plan.items,
        start=1
    ):

        print(
            f"\n{index}. {item.subject}"
        )

        print(
            f"   Time: {item.hours} hours"
        )

        print(
            f"   Priority: {item.priority}"
        )

        total_hours += item.hours

    print(
        "\n-------------------------------------"
    )

    print(
        f"Total study time: {total_hours} hours"
    )

    print(
        f"Attempts: {state['attempt']}"
    )

    print(
        "-------------------------------------"
    )

    # ------------------------------------------
    # Now collect session feedback
    # ------------------------------------------

    print(
        "\n========== SESSION FEEDBACK =========="
    )

    print(
        "Which subjects did you complete?"
    )

    print(
        "Available subjects:"
    )

    print(
        state["subjects"]
    )

    completed_input = input(
        "\nCompleted subjects "
        "(comma separated, or press Enter for none): "
    ).strip()

    print(
        "\nWhich subjects did you skip?"
    )

    skipped_input = input(
        "Skipped subjects "
        "(comma separated, or press Enter for none): "
    ).strip()

    completed_subjects = [
        subject.strip()
        for subject in completed_input.split(",")
        if subject.strip()
    ]

    skipped_subjects = [
        subject.strip()
        for subject in skipped_input.split(",")
        if subject.strip()
    ]

    feedback = SessionFeedback(
        completed_subjects=completed_subjects,
        skipped_subjects=skipped_subjects
    )

    planned_subjects = [
        subject.strip()
        for subject in state["subjects"].split(",")
        if subject.strip()
    ]

    is_valid, error_message = (
        validate_session_feedback(
            feedback,
            planned_subjects
        )
    )

    if not is_valid:

        print(
            f"\nSession feedback rejected:\n"
            f"{error_message}\n\n"
            f"Please enter only subjects from the current study plan.\n\n"
            f"Available subjects:\n"
            f"{state['subjects']}"
        )

        return {
            "session_feedback": None,
            "session": None,
            "session_error": error_message
        }

    plan = state["plan"]

    planned_hours = sum(
        item.hours
        for item in plan.items
    )

    session = create_session_memory(
        subjects=planned_subjects,
        planned_hours=planned_hours,
        completed_subjects=completed_subjects,
        skipped_subjects=skipped_subjects
    )

    print(
        "\nSession feedback accepted."
    )

    return {
        "session_feedback": feedback,
        "session": session,
        "session_error": ""
    }