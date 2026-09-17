from state import StudyState

from llm import structured_planner, structured_critic

from prompts import planner_prompt, critic_prompt



def generate_plan(state: StudyState):
    attempt = state["attempt"] + 1

    messages = planner_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "feedback": state["feedback"]
    })

    response = structured_planner.invoke(messages)

    print(f"\nGenerating study plan. Attempt: {attempt}")

    return {
        "plan": response,
        "attempt": attempt
    }


def validate_plan(state: StudyState):
    plan = state["plan"]

    total_hours = sum(
        item.hours for item in plan.items
    )

    available_hours = state["hours"]

    if total_hours > available_hours:
        print("Plan validation failed.")

        return {
            "review_status": "IMPROVE",
            "feedback": (
                f"The plan uses {total_hours} hours, "
                f"but only {available_hours} hours are available. "
                "Reduce the study time."
            )
        }

    print("Plan validation passed.")

    return {
        "review_status": "VALID",
        "feedback": ""
    }


def critique_plan(state: StudyState):
    messages = critic_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "plan": state["plan"]
    })

    review = structured_critic.invoke(messages)

    print("AI critic reviewed the plan.")

    return {
        "review_status": review.status,
        "feedback": review.feedback
    }

def decide_after_validation(state: StudyState):
    if state["review_status"] == "IMPROVE":
        if state["attempt"] >= 3:
            return "critic"

        return "retry"

    return "critic"

def decide_after_critique(state: StudyState):
    if state["review_status"] == "GOOD":
        return "good"

    if state["attempt"] >= 3:
        return "good"

    return "retry"



  