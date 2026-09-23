from datetime import datetime


def create_session_memory(
    subjects,
    planned_hours,
    completed_subjects,
    skipped_subjects
):
    """
    Create a memory record for a study session.
    """

    return {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "subjects": subjects,
        "planned_hours": planned_hours,
        "completed_subjects": completed_subjects,
        "skipped_subjects": skipped_subjects
    }