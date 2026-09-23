from models import SessionFeedback
from typing import TypedDict

from models import (
    StudyPlan,
    SubjectPriority,
    PlanEvaluation,
    WorkflowError,
    ExecutionTrace
)


class StudyState(TypedDict):
    hours: float
    subjects: str
    level: str
    priorities: list[SubjectPriority]

    memory_context: str
    memory_insights: str
    session_feedback: SessionFeedback | None

    session: dict | None

    session_error: str
    plan: StudyPlan | None

    evaluation: PlanEvaluation | None

    feedback: str
    validation_status: str
    decision: str
    retry_reason: str

    error: WorkflowError | None

    execution_trace: list[ExecutionTrace]

    attempt: int