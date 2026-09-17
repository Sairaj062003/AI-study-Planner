from nodes import decide_after_validation
from nodes import validate_plan
from nodes import decide_after_critique
from nodes import critique_plan
from langgraph.graph import StateGraph
from state import StudyState
from nodes import generate_plan
from langgraph.graph import START , END



builder = StateGraph(StudyState)
builder.add_node("generate_plan", generate_plan)
builder.add_node("critique_plan", critique_plan)
builder.add_node("validate_plan", validate_plan)



builder.add_edge(START, "generate_plan")
builder.add_edge("generate_plan", "validate_plan")

builder.add_conditional_edges(
    "validate_plan",
    decide_after_validation,
    {
        "retry": "generate_plan",
        "critic": "critique_plan"
    }
)

builder.add_conditional_edges(
    "critique_plan",
    decide_after_critique,
    {
        "good": END,
        "retry": "generate_plan"
    }
)


graph = builder.compile()




