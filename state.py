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

    plan: StudyPlan | None

    evaluation: PlanEvaluation | None

    feedback: str

    validation_status: str
    decision: str
    retry_reason: str

    error: WorkflowError | None

    execution_trace: list[ExecutionTrace]

    attempt: int