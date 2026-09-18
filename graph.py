from langgraph.graph import (
    StateGraph,
    START,
    END
)

from state import StudyState

from nodes import (
    generate_plan,
    validate_plan,
    evaluate_plan,
    decision_engine
)


builder = StateGraph(
    StudyState
)


builder.add_node(
    "generate_plan",
    generate_plan
)

builder.add_node(
    "validate_plan",
    validate_plan
)

builder.add_node(
    "evaluate_plan",
    evaluate_plan
)

builder.add_node(
    "decision_engine",
    decision_engine
)


builder.add_edge(
    START,
    "generate_plan"
)


builder.add_edge(
    "generate_plan",
    "validate_plan"
)


def route_after_validation(state):
    if state["validation_status"] == "VALID":
        return "evaluate"

    return "decision"

builder.add_conditional_edges(
    "validate_plan",
    route_after_validation,
    {
        "evaluate": "evaluate_plan",
        "decision": "decision_engine"
    }
)

builder.add_edge(
    "evaluate_plan",
    "decision_engine"
)


builder.add_conditional_edges(
    "decision_engine",
    lambda state: state["decision"],
    {
        "ACCEPT": END,
        "RETRY": "generate_plan",
        "FAIL": END
    }
)


graph = builder.compile()