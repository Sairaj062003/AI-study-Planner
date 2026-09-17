from pydantic import BaseModel, Field


class StudyItem(BaseModel):
    subject: str = Field(description="Subject to study")
    hours: float = Field(description="Hours to spend on the subject")
    priority: str = Field(description="Priority: High, Medium, or Low")


class StudyPlan(BaseModel):
    items: list[StudyItem]

class PlanReview(BaseModel):
    status: str = Field(description="Either GOOD or IMPROVE")
    feedback: str = Field(description="Short explanation of the review")