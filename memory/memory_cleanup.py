MIN_EVIDENCE_COUNT = 2


def cleanup_learned_patterns(
    memory
):
    """
    Remove weak learned patterns
    and update their importance.
    """

    patterns = memory.get(
        "learned_patterns",
        []
    )

    cleaned_patterns = []

    for pattern in patterns:

        evidence_count = pattern.get(
            "evidence_count",
            1
        )

        if evidence_count < MIN_EVIDENCE_COUNT:
            continue

        if evidence_count >= 3:

            pattern["importance"] = "high"

        else:

            pattern["importance"] = "medium"

        cleaned_patterns.append(
            pattern
        )

    memory["learned_patterns"] = (
        cleaned_patterns
    )

    return memory