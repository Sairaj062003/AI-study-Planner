def analyze_sessions(sessions):
    """
    Analyze previous study sessions
    and produce structured planning insights.
    """

    if not sessions:
        return []

    subject_stats = {}

    for session in sessions:

        for subject in session.get(
            "subjects",
            []
        ):

            if subject not in subject_stats:

                subject_stats[subject] = {
                    "planned": 0,
                    "completed": 0,
                    "skipped": 0
                }

            subject_stats[subject]["planned"] += 1

        for subject in session.get(
            "completed_subjects",
            []
        ):

            if subject not in subject_stats:

                subject_stats[subject] = {
                    "planned": 0,
                    "completed": 0,
                    "skipped": 0
                }

            subject_stats[subject]["completed"] += 1

        for subject in session.get(
            "skipped_subjects",
            []
        ):

            if subject not in subject_stats:

                subject_stats[subject] = {
                    "planned": 0,
                    "completed": 0,
                    "skipped": 0
                }

            subject_stats[subject]["skipped"] += 1

    insights = []

    for subject, stats in subject_stats.items():

        if stats["skipped"] > stats["completed"]:

            insights.append({
                "type": "pattern",
                "subject": subject,
                "information": (
                    f"{subject} has frequently been skipped "
                    "in previous sessions."
                ),
                "importance": "medium"
            })

        elif stats["completed"] > 0:

            insights.append({
                "type": "pattern",
                "subject": subject,
                "information": (
                    f"{subject} has been completed successfully "
                    "in previous sessions."
                ),
                "importance": "medium"
            })

    return insights