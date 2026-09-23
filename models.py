from pydantic import BaseModel, Field

class SubjectPriority(BaseModel):
    subject: str = Field(
        description="Subject to study"
    )

    priority: str = Field(
        description="Priority: High, Medium, or Low"
    )

class UserRequest(BaseModel):
    hours: float = Field(
        description="Number of hours available for studying"
    )

    subjects: list[str] = Field(
        description="List of subjects the student wants to study"
    )

    level: str = Field(
        description="Student level: Beginner, Intermediate, or Advanced"
    )

    priorities: list[SubjectPriority] = Field(
        description="List of subjects with their priorities"
    )


class StudyItem(BaseModel):
    subject: str = Field(
        description="Subject to study"
    )

    hours: float = Field(
        description="Hours to spend on the subject"
    )

    priority: str = Field(
        description="Priority: High, Medium, or Low"
    )


class StudyPlan(BaseModel):
    items: list[StudyItem]


class PlanEvaluation(BaseModel):
    time_fit_score: int = Field(
        description="Score from 1 to 10 for how appropriately study time is distributed"
    )

    subject_coverage_score: int = Field(
        description="Score from 1 to 10 for how well the plan covers all requested subjects"
    )

    priority_alignment_score: int = Field(
        description="Score from 1 to 10 for how well the plan follows subject priorities"
    )

    level_suitability_score: int = Field(
        description="Score from 1 to 10 for how suitable the plan is for the student's level"
    )

    realism_score: int = Field(
        description="Score from 1 to 10 for how realistic and practical the plan is"
    )
    memory_consistency_score: int = Field(
        description=(
            "Score from 1 to 10 for how appropriately "
            "the plan uses relevant historical memory "
            "without allowing memory to override the "
            "current request"
        )
    )

    overall_feedback: str = Field(
        description="Short explanation of the plan quality and what could be improved"
    )

class WorkflowError(BaseModel):
    error_type: str = Field(
        description="Type of workflow error"
    )

    message: str = Field(
        description="Human-readable explanation of the error"
    )

    recoverable: bool = Field(
        description="Whether the workflow can retry after this error"
    )

class ExecutionTrace(BaseModel):
    attempt: int

    validation_status: str

    time_fit_score: int | None = None

    subject_coverage_score: int | None = None

    priority_alignment_score: int | None = None

    level_suitability_score: int | None = None

    realism_score: int | None = None

    memory_consistency_score: int | None = None

    decision: str

    reason: str = ""

    error_type: str | None = None

    error_message: str | None = None

class MemoryUpdate(BaseModel):
    memory_type: str = Field(
        description="Type of memory: preference or pattern"
    )

    subject: str = Field(
        description="Subject related to the memory"
    )

    information: str = Field(
        description="Information learned from the study history"
    )

    importance: str = Field(
        description="Importance of the memory: low, medium, or high"
    )    

class SessionFeedback(BaseModel):
    completed_subjects: list[str] = Field(
        description="Subjects the student actually completed"
    )

    skipped_subjects: list[str] = Field(
        description="Subjects the student skipped"
    )

