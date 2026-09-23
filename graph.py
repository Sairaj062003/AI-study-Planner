from langgraph.graph import (
    StateGraph,
    START,
    END
)
from nodes.session import (
    collect_session_feedback
)
from nodes.memory_writer import (
    write_session_memory
)
from nodes.memory import retrieve_memory
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
    "retrieve_memory",
    retrieve_memory
)
builder.add_node(
    "collect_session_feedback",
    collect_session_feedback
)
builder.add_node(
    "generate_plan",
    generate_plan
)
builder.add_node(
    "write_session_memory",
    write_session_memory
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
    "retrieve_memory"
)

builder.add_edge(
    "retrieve_memory",
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
        "ACCEPT": "collect_session_feedback",
        "RETRY": "generate_plan",
        "FAIL": END
    }
)
builder.add_edge(
    "collect_session_feedback",
    "write_session_memory"
)

builder.add_edge(
    "write_session_memory",
    END
)

graph = builder.compile()