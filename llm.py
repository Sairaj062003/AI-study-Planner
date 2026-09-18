from models import PlanEvaluation
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from models import (
    UserRequest,
    StudyPlan,
    PlanEvaluation
)


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


structured_request_parser = model.with_structured_output(
    UserRequest
)


structured_planner = model.with_structured_output(
    StudyPlan
)


structured_evaluator = model.with_structured_output(
    PlanEvaluation
)         