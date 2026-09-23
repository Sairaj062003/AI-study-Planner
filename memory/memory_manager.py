import json
from pathlib import Path
from memory.memory_cleanup import (
    cleanup_learned_patterns
)


MEMORY_FILE = Path(__file__).parent / "memory.json"


def load_memory():
    """
    Load persistent memory from memory.json.
    """

    if not MEMORY_FILE.exists():

        return {
            "sessions": [],
            "preferences": {},
            "learned_patterns": []
        }

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        memory = json.load(file)

    memory.setdefault(
        "sessions",
        []
    )

    memory.setdefault(
        "preferences",
        {}
    )

    memory.setdefault(
        "learned_patterns",
        []
    )

    return memory

def save_memory(memory):
    """
    Save persistent memory to memory.json.
    """

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )

def add_session(memory, session):
    """
    Add a study session to persistent memory.
    """

    memory["sessions"].append(session)

    return memory

def save_session_and_learn(
    memory,
    session,
    insights
):
    """
    Save a completed study session,
    update learned patterns,
    and clean weak memories.
    """

    memory["sessions"].append(
        session
    )

    from memory.memory_updater import (
        update_learned_patterns
    )

    memory = update_learned_patterns(
        memory,
        insights
    )

    memory = cleanup_learned_patterns(
        memory
    )

    save_memory(
        memory
    )

    return memory