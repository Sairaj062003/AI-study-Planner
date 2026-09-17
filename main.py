from graph import graph

from nodes import parse_user_request


def display_plan(result):
    """
    Display the final study plan.
    """

    plan = result["plan"]

    print(
        "\n========== YOUR STUDY PLAN =========="
    )

    total_hours = 0

    for index, item in enumerate(
        plan.items,
        start=1
    ):

        print(
            f"\n{index}. {item.subject}"
        )

        print(
            f"   Time: {item.hours} hours"
        )

        print(
            f"   Priority: {item.priority}"
        )

        total_hours += item.hours

    print(
        "\n-------------------------------------"
    )

    print(
        f"Total study time: {total_hours} hours"
    )

    print(
        f"Attempts: {result['attempt']}"
    )

    print(
        "-------------------------------------"
    )


def main():

    print(
        "========== AI STUDY PLANNER =========="
    )

    print(
        "\nDescribe your study requirements."
    )

    print(
        "Example:"
    )

    print(
        "I have 4 hours today. "
        "I need to study Python, DSA and LangChain. "
        "Python is more important because I have "
        "an interview next week."
    )

    print()

    user_request = input(
        "Your request: "
    ).strip()


    # Basic input validation
    if not user_request:

        print(
            "Please enter a study request."
        )

        return


    # ---------------------------------
    # STEP 1: Parse natural language
    # ---------------------------------

    print(
        "\nUnderstanding your request..."
    )

    parsed_request = parse_user_request(
        user_request
    )


    print(
        "\n========== REQUEST UNDERSTOOD =========="
    )

    print(
        f"Available hours: "
        f"{parsed_request.hours}"
    )

    print(
        f"Subjects: "
        f"{', '.join(parsed_request.subjects)}"
    )

    print(
        f"Level: "
        f"{parsed_request.level}"
    )

    print(
        f"Priorities: "
        f"{parsed_request.priorities}"
    )


    # ---------------------------------
    # STEP 2: Convert parsed request
    # into LangGraph state
    # ---------------------------------

    subjects = ", ".join(
        parsed_request.subjects
    )


    initial_state = {
        "hours": parsed_request.hours,

        "subjects": subjects,

        "level": parsed_request.level,

        "priorities": parsed_request.priorities,

        "plan": None,

        "feedback": "",

        "review_status": "",

        "attempt": 0
    }


    # ---------------------------------
    # STEP 3: Run LangGraph
    # ---------------------------------

    print(
        "\nStarting study planner..."
    )

    result = graph.invoke(
        initial_state
    )


    # ---------------------------------
    # STEP 4: Display final result
    # ---------------------------------

    display_plan(result)


    print(
        "\n========== AI REVIEW =========="
    )

    print(
        result["feedback"]
    )


if __name__ == "__main__":
    main()