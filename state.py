from models import PlanReview
from models import StudyPlan
from typing import TypedDict, Any

class StudyState(TypedDict):

    hours: float
    subjects: str
    level: str
    plan: StudyPlan | None
    feedback: str
    review_status: PlanReview | None
    attempt: int

