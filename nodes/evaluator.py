from nodes import format_priorities
from state import StudyState

from llm import structured_evaluator

from prompts import evaluator_prompt

from error_handler import create_workflow_error

def evaluate_plan(state: StudyState):
    """
    Ask Gemini to evaluate the quality of the generated study plan.
    """

    plan = state["plan"]

    messages = evaluator_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "priorities": format_priorities(
            state["priorities"]
        ),
        "memory_context": state.get("memory_context", ""),
        "memory_insights": state.get("memory_insights", ""),
        "plan": plan.model_dump()
    })

    try:

        evaluation = structured_evaluator.invoke(
            messages
        )

        print(
            "AI evaluator reviewed the plan."
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

        return {
            "evaluation": evaluation,
            "feedback": evaluation.overall_feedback,
            "error": None
        }

    except Exception as error:

        print(
            "AI evaluation failed."
        )

        workflow_error = create_workflow_error(
            error_type="LLM_EVALUATION_ERROR",
            message=str(error),
            recoverable=True
        )

        return {
            "evaluation": None,
            "error": workflow_error
        }
