from typing import TypedDict

from models import StudyPlan


class StudyState(TypedDict):
    hours: float
    subjects: str
    level: str
    priorities: str

    plan: StudyPlan | None

    feedback: str
    review_status: str

    attempt: int