from langgraph.graph import (
    StateGraph,
    START,
    END
)

from state import StudyState

from nodes import (
    generate_plan,
    validate_plan,
    critique_plan,
    decide_after_validation,
    decide_after_critique
)


# Create the graph
builder = StateGraph(StudyState)


# Add nodes
builder.add_node(
    "generate_plan",
    generate_plan
)

builder.add_node(
    "validate_plan",
    validate_plan
)

builder.add_node(
    "critique_plan",
    critique_plan
)


# START → Generate Plan
builder.add_edge(
    START,
    "generate_plan"
)


# Generate Plan → Validate Plan
builder.add_edge(
    "generate_plan",
    "validate_plan"
)


# Validation decision
builder.add_conditional_edges(
    "validate_plan",
    decide_after_validation,
    {
        "critic": "critique_plan",
        "retry": "generate_plan"
    }
)


# Critic decision
builder.add_conditional_edges(
    "critique_plan",
    decide_after_critique,
    {
        "good": END,
        "retry": "generate_plan"
    }
)


# Compile graph
graph = builder.compile()