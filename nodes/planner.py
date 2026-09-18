from llm import structured_planner
from state import StudyState
from nodes import format_priorities
from prompts import planner_prompt
from error_handler import create_workflow_error
def generate_plan(state: StudyState):
    """
    Generate a structured study plan using Gemini.
    """

    attempt = state["attempt"] + 1

    print(
        f"\nGenerating study plan. Attempt: {attempt}"
    )

    messages = planner_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "priorities": format_priorities(
            state["priorities"]
        ),
        "feedback": state["feedback"]
    })

    try:

        response = structured_planner.invoke(
            messages
        )

        return {
            "plan": response,
            "attempt": attempt,
            "error": None
        }

    except Exception as error:

        print(
            "Plan generation failed."
        )

        workflow_error = create_workflow_error(
            error_type="LLM_GENERATION_ERROR",
            message=str(error),
            recoverable=True
        )

        return {
            "plan": None,
            "attempt": attempt,
            "error": workflow_error
        }
