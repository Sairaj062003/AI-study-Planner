def retrieve_recent_sessions(
    memory,
    limit=3
):
    """
    Retrieve the most recent study sessions.
    """

    sessions = memory.get(
        "sessions",
        []
    )

    if not sessions:
        return []

    return sessions[-limit:]

def retrieve_subject_sessions(
    memory,
    subjects,
    limit=5
):
    """
    Retrieve previous sessions
    containing the requested subjects.
    """

    sessions = memory.get(
        "sessions",
        []
    )

    requested_subjects = {
        subject.strip().lower()
        for subject in subjects
    }

    relevant_sessions = []

    for session in sessions:

        session_subjects = {
            subject.strip().lower()
            for subject in session.get(
                "subjects",
                []
            )
        }

        if requested_subjects.intersection(
            session_subjects
        ):
            relevant_sessions.append(
                session
            )

    return relevant_sessions[-limit:]

def format_memories(sessions):
    """
    Convert retrieved memories into text
    for the AI planner.
    """

    if not sessions:
        return "No previous study sessions found."

    lines = []

    for session in sessions:

        lines.append(
            f"Date: {session['date']}"
        )

        lines.append(
            f"Subjects: "
            f"{', '.join(session['subjects'])}"
        )

        lines.append(
            f"Planned hours: "
            f"{session['planned_hours']}"
        )

        lines.append(
            f"Completed: "
            f"{', '.join(session['completed_subjects'])}"
        )

        lines.append(
            f"Skipped: "
            f"{', '.join(session['skipped_subjects'])}"
        )

        lines.append("")

    return "\n".join(lines)

def retrieve_learned_patterns(
    memory,
    limit=5
):
    """
    Retrieve the strongest learned patterns.
    """

    patterns = memory.get(
        "learned_patterns",
        []
    )

    sorted_patterns = sorted(
        patterns,
        key=lambda pattern: (
            pattern.get(
                "evidence_count",
                1
            ),
            pattern.get(
                "importance",
                "low"
            )
        ),
        reverse=True
    )

    return sorted_patterns[:limit]

def format_learned_patterns(
    patterns
):
    """
    Convert learned patterns into text
    for the AI planner.
    """

    if not patterns:

        return (
            "No strong learned patterns available."
        )

    lines = []

    for pattern in patterns:

        lines.append(
            f"- {pattern['information']} "
            f"(evidence: "
            f"{pattern.get('evidence_count', 1)})"
        )

    return "\n".join(lines)