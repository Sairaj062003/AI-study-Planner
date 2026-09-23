from memory.memory_retriever import retrieve_learned_patterns
from memory.memory_retriever import format_learned_patterns
from state import StudyState

from memory.memory_manager import load_memory
from memory.memory_analyzer import (
    analyze_sessions
)

from memory.memory_retriever import (
    retrieve_subject_sessions,
    format_memories
)


def retrieve_memory(state: StudyState):
    """
    Retrieve relevant historical sessions
    and learned patterns.
    """

    memory = load_memory()

    subjects = [
        subject.strip()
        for subject in state["subjects"].split(",")
        if subject.strip()
    ]

    sessions = retrieve_subject_sessions(
        memory,
        subjects
    )

    patterns = retrieve_learned_patterns(
        memory
    )

    memory_context = format_memories(
        sessions
    )

    memory_insights = format_learned_patterns(
        patterns
    )

    print(
        "\nMemory retrieved."
    )

    print(
        f"Relevant sessions: {len(sessions)}"
    )

    print(
        f"Learned patterns: {len(patterns)}"
    )

    return {
        "memory_context": memory_context,
        "memory_insights": memory_insights
    }