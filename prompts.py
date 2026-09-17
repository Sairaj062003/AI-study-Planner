from langchain_core.prompts import ChatPromptTemplate


planner_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI study planner.

    Create a practical study plan for a student.

    Available study time: {hours} hours.
    Subjects: {subjects}.
    Student level: {level}.

    Previous feedback:
    {feedback}

    Create a simple and realistic study plan.

    Include every requested subject.

    Make sure the total study time does not exceed
    the available study time.
    """
)


critic_prompt = ChatPromptTemplate.from_template(
    """
    You are a study plan reviewer.

    Review the following study plan.

    Available study time: {hours} hours.
    Subjects: {subjects}.
    Student level: {level}.

    Study plan:
    {plan}

    Check:

    1. The total study time.
    2. Whether all requested subjects are included.
    3. Whether the plan matches the student's level.
    4. Whether the time distribution is reasonable.

    If the plan is reasonable, return GOOD.

    If the plan needs improvement, return IMPROVE
    and explain what should be changed.
    """
)