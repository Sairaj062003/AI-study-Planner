def update_learned_patterns(
    memory,
    insights
):
    """
    Add new patterns or strengthen
    existing patterns.
    """

    patterns = memory.setdefault(
        "learned_patterns",
        []
    )

    for insight in insights:

        existing_pattern = None

        for pattern in patterns:

            if (
                pattern["subject"]
                == insight["subject"]
                and
                pattern["information"]
                == insight["information"]
            ):
                existing_pattern = pattern
                break

        if existing_pattern:

            existing_pattern["evidence_count"] += 1

        else:

            patterns.append({
                "type": insight["type"],
                "subject": insight["subject"],
                "information": insight["information"],
                "importance": insight["importance"],
                "evidence_count": 1
            })

    return memory