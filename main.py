from graph import graph

from nodes import parse_user_request

from harness.input_validator import validate_user_request




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
    

    is_valid,error_message = validate_user_request(user_request)
    
    if not is_valid:
        print(
            error_message
        )
        return

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

    print("Priorities:")

    for priority in parsed_request.priorities:
        print(
            f"{priority.subject}: "
            f"{priority.priority}"
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

    "validation_status": "",

    "evaluation": None,

    "decision": "",

    "retry_reason": "",

    "error": None,

    "execution_trace": [],

    "memory_context": "",

    "memory_insights": "",

    "session_feedback": None,

    "session": None,

    "session_error": "",

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
    # STEP 4: Display evaluation summary
    # and execution trace
    # ---------------------------------

    evaluation = result["evaluation"]

    print(
        "\n========== AI EVALUATION =========="
    )

    print(
        f"Time fit: "
        f"{evaluation.time_fit_score}/10"
    )

    print(
        f"Subject coverage: "
        f"{evaluation.subject_coverage_score}/10"
    )

    print(
        f"Priority alignment: "
        f"{evaluation.priority_alignment_score}/10"
    )

    print(
        f"Level suitability: "
        f"{evaluation.level_suitability_score}/10"
    )

    print(
        f"Realism: "
        f"{evaluation.realism_score}/10"
    )

    print(
        f"Memory consistency: "
        f"{evaluation.memory_consistency_score}/10"
    )

    print(
        "\nFeedback:"
    )

    print(
        evaluation.overall_feedback
    )

    display_execution_trace(
        result
    )


def display_execution_trace(result):
    """
    Display the execution history of the workflow.
    """

    print(
        "\n========== EXECUTION TRACE =========="
    )

    for trace in result["execution_trace"]:

        print(
            f"\nAttempt {trace.attempt}"
        )

        print(
            f"Validation: "
            f"{trace.validation_status}"
        )

        if trace.time_fit_score is not None:

            print(
                f"Time fit: "
                f"{trace.time_fit_score}/10"
            )

            print(
                f"Subject coverage: "
                f"{trace.subject_coverage_score}/10"
            )

            print(
                f"Priority alignment: "
                f"{trace.priority_alignment_score}/10"
            )

            print(
                f"Level suitability: "
                f"{trace.level_suitability_score}/10"
            )

            print(
                f"Realism: "
                f"{trace.realism_score}/10"
            )

            if trace.memory_consistency_score is not None:

                print(
                    f"Memory consistency: "
                    f"{trace.memory_consistency_score}/10"
                )

        print(
            f"Decision: "
            f"{trace.decision}"
        )

        if trace.reason:

            print(
                f"Reason: "
                f"{trace.reason}"
            )

        if trace.error_type:

            print(
                f"Error type: "
                f"{trace.error_type}"
            )

            print(
                f"Error message: "
                f"{trace.error_message}"
            )


if __name__ == "__main__":
    main()

