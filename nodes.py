from state import StudyState

from llm import (
    structured_request_parser,
    structured_planner,
    structured_critic
)

from prompts import (
    request_parser_prompt,
    planner_prompt,
    critic_prompt
)


def parse_user_request(user_request: str):
    """
    Convert a natural-language user request
    into structured UserRequest data.
    """

    messages = request_parser_prompt.invoke({
        "user_request": user_request
    })

    response = structured_request_parser.invoke(
        messages
    )

    return response


def generate_plan(state: StudyState):
    """
    Generate a structured study plan using Gemini.
    """

    attempt = state["attempt"] + 1

    messages = planner_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "priorities": state["priorities"],
        "feedback": state["feedback"]
    })

    response = structured_planner.invoke(
        messages
    )

    print(
        f"\nGenerating study plan. Attempt: {attempt}"
    )

    return {
        "plan": response,
        "attempt": attempt
    }


def validate_plan(state: StudyState):
    """
    Deterministically validate the generated plan.
    """

    plan = state["plan"]

    if plan is None:
        return {
            "review_status": "IMPROVE",
            "feedback": "No study plan was generated."
        }

    total_hours = sum(
        item.hours
        for item in plan.items
    )

    available_hours = state["hours"]

    # Check total study time
    if total_hours > available_hours:

        print("Plan validation failed.")

        return {
            "review_status": "IMPROVE",
            "feedback": (
                f"The plan uses {total_hours} hours, "
                f"but only {available_hours} hours "
                "are available. Reduce the study time."
            )
        }

    # Check for negative or zero hours
    for item in plan.items:

        if item.hours <= 0:

            print("Plan validation failed.")

            return {
                "review_status": "IMPROVE",
                "feedback": (
                    f"{item.subject} has an invalid "
                    "study duration."
                )
            }

    print("Plan validation passed.")

    return {
        "review_status": "VALID",
        "feedback": ""
    }


def critique_plan(state: StudyState):
    """
    Ask Gemini to review the generated study plan.
    """

    plan = state["plan"]

    messages = critic_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "priorities": state["priorities"],
        "plan": plan.model_dump()
    })

    review = structured_critic.invoke(
        messages
    )

    print("AI critic reviewed the plan.")

    return {
        "review_status": review.status.upper(),
        "feedback": review.feedback
    }


def decide_after_validation(state: StudyState):
    """
    Decide whether the plan should go to the
    AI critic or be generated again.
    """

    if state["review_status"] == "IMPROVE":

        if state["attempt"] >= 3:
            return "critic"

        return "retry"

    return "critic"


def decide_after_critique(state: StudyState):
    """
    Decide whether the workflow should finish
    or generate another plan.
    """

    if state["review_status"] == "GOOD":
        return "good"

    if state["attempt"] >= 3:
        return "good"

    return "retry"