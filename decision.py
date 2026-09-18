MAX_ATTEMPTS = 3

MIN_TIME_FIT_SCORE = 7
MIN_SUBJECT_COVERAGE_SCORE = 7
MIN_PRIORITY_ALIGNMENT_SCORE = 7
MIN_LEVEL_SUITABILITY_SCORE = 7
MIN_REALISM_SCORE = 7


def decide_from_evaluation(evaluation):
    """
    Decide whether the plan quality is good enough
    and explain why a retry is required.
    """

    failures = []


    if evaluation.time_fit_score < MIN_TIME_FIT_SCORE:
        failures.append(
            "Time distribution needs improvement."
        )


    if evaluation.subject_coverage_score < MIN_SUBJECT_COVERAGE_SCORE:
        failures.append(
            "Subject coverage needs improvement."
        )


    if evaluation.priority_alignment_score < MIN_PRIORITY_ALIGNMENT_SCORE:
        failures.append(
            "Priority alignment needs improvement."
        )


    if evaluation.level_suitability_score < MIN_LEVEL_SUITABILITY_SCORE:
        failures.append(
            "The plan is not sufficiently suitable for the student's level."
        )


    if evaluation.realism_score < MIN_REALISM_SCORE:
        failures.append(
            "The plan is not sufficiently realistic."
        )


    if not failures:
        return "ACCEPT", ""


    retry_reason = " ".join(failures)

    return "RETRY", retry_reason

def decide_next_action(state):
    """
    Decide whether the workflow should accept,
    retry, or fail.
    """


    error = state["error"]

    if error is not None:

        if not error.recoverable:
            return (
                "FAIL",
                error.message
            )

        if state["attempt"] >= MAX_ATTEMPTS:
            return (
                "FAIL",
                "Maximum attempts reached after "
                "workflow errors."
            )

        return (
            "RETRY",
            "The previous operation failed. "
            "Retrying the workflow."
        )

    if state["validation_status"] == "VALID":

        evaluation = state["evaluation"]

        if evaluation is None:
            return (
                "FAIL",
                "AI evaluation was not available."
            )


        decision, reason = decide_from_evaluation(
            evaluation
        )


        if decision == "ACCEPT":
            return "ACCEPT", ""


        if state["attempt"] >= MAX_ATTEMPTS:

            return (
                "FAIL",
                "Maximum retry attempts reached. "
                "The generated plan still requires improvement."
            )


        return "RETRY", reason


    if state["attempt"] >= MAX_ATTEMPTS:

        return (
            "FAIL",
            "Maximum retry attempts reached because "
            "the generated plan failed deterministic validation."
        )


    return (
        "RETRY",
        state["feedback"]
    )


