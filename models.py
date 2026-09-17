from pydantic import BaseModel, Field


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

    priorities: str = Field(
        description="Important priorities, preferences, or reasons mentioned by the student"
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


class PlanReview(BaseModel):
    status: str = Field(
        description="Either GOOD or IMPROVE"
    )

    feedback: str = Field(
        description="Short explanation of the review"
    )