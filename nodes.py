from models import PlanReview
from models import StudyPlan
from state import StudyState
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
structured_model = model.with_structured_output(StudyPlan)
structured_critic = model.with_structured_output(PlanReview)
planner_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI study planner.

    Create a practical study plan for a student.

    Available study time: {hours} hours.
    Subjects: {subjects}.
    Student level: {level}.

    Previous feedback:
    {feedback}

    Create a simple study plan.
    Include the subject and recommended time for each subject.
    """
)

def generate_plan(state: StudyState):
    attempt = state['attempt']+1

    messages = planner_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "feedback":state['feedback']
    })

    response = structured_model.invoke(messages)

    return {
        "plan": response,
        "attempt":attempt
    }

critic_prompt = ChatPromptTemplate.from_template(
    """
    You are a study plan reviewer.

    Review the following study plan.

    Available study time: {hours} hours.
    Subjects: {subjects}.
    Student level: {level}.

    Study plan:
    {plan}

    Check whether:
    1. The total study time is reasonable.
    2. All requested subjects are included.
    3. The plan is appropriate for the student's level.
    4. The time distribution makes sense.

    If the plan is reasonable, return status GOOD.

    If the plan needs improvement, return status IMPROVE
    and explain what should be changed.
    """
)

def critique_plan(state: StudyState):
    messages = critic_prompt.invoke({
        "hours": state["hours"],
        "subjects": state["subjects"],
        "level": state["level"],
        "plan": state["plan"]
    })

    review = structured_critic.invoke(messages)

    return {
        "review_status":review.status,
         "feedback": review.feedback
    }

    if feedback.strip().upper().startswith("GOOD"):
        return {
            "feedback": feedback
        }

    return {
        "feedback": feedback
    }

def decide_after_critique(state: StudyState):
    if state["review_status"] == "GOOD":
        return "good"

    if state["attempt"] >= 3:
        return "good"

    return "retry"



  