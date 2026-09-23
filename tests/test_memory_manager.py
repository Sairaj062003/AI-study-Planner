from memory.memory_manager import (
    load_memory,
    save_memory
)


def test_memory_can_be_loaded():

    memory = load_memory()

    assert "sessions" in memory
    assert "preferences" in memory


def test_memory_can_be_saved():

    memory = {
        "sessions": [],
        "preferences": {
            "test": "value"
        }
    }

    save_memory(memory)

    loaded_memory = load_memory()

    assert loaded_memory["preferences"]["test"] == "value"