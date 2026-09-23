from state import StudyState

from memory.memory_manager import (
    load_memory,
    save_session_and_learn
)

from memory.memory_analyzer import (
    analyze_sessions
)


def write_session_memory(
    state: StudyState
):
    """
    Save the completed study session
    and update learned memory.
    """

    session = state["session"]

    if session is None:

        return {}

    memory = load_memory()

    insights = analyze_sessions(
        memory["sessions"] + [session]
    )

    memory = save_session_and_learn(
        memory,
        session,
        insights
    )

    print(
        "\nStudy session saved to memory."
    )

    print(
        "Memory updated."
    )

    return {
        "memory_insights": "\n".join(
            insight["information"]
            for insight in insights
        )
    }