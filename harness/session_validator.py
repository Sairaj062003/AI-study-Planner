def validate_session_feedback(
    feedback,
    planned_subjects
):
    """
    Validate the user's session feedback.
    """

    planned = {
        subject.strip().lower()
        for subject in planned_subjects
    }

    completed = {
        subject.strip().lower()
        for subject in feedback.completed_subjects
    }

    skipped = {
        subject.strip().lower()
        for subject in feedback.skipped_subjects
    }

    if completed.intersection(skipped):

        return False, (
            "A subject cannot be both completed "
            "and skipped."
        )

    unknown_subjects = (
        completed | skipped
    ) - planned

    if unknown_subjects:

        return False, (
            "These subjects were not part of "
            "the study plan: "
            + ", ".join(
                sorted(unknown_subjects)
            )
        )

    return True, ""