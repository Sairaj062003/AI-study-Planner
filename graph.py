from nodes import decide_after_critique
from nodes import critique_plan
from langgraph.graph import StateGraph
from state import StudyState
from nodes import generate_plan
from langgraph.graph import START , END



builder = StateGraph(StudyState)
builder.add_node("generate_plan", generate_plan)
builder.add_node("critique_plan", critique_plan)



builder.add_edge(START, "generate_plan")
builder.add_edge("generate_plan", "critique_plan")

builder.add_conditional_edges(
    "critique_plan",
    decide_after_critique,
    {
        "good": END,
        "retry": "generate_plan"
    }
)


graph = builder.compile()


initial_state = {
    "hours": 4,
    "subjects": "Python, DSA and LangChain",
    "level": "Beginner",
    "plan": None,
    "feedback": "",
    "attempt": 0
}

result = graph.invoke(initial_state)

print("\n========== FINAL STUDY PLAN ==========")

for item in result["plan"].items:
    print(
        f"{item.subject}: "
        f"{item.hours} hours - "
        f"{item.priority} priority"
    )

print("\nAttempts:", result["attempt"])

