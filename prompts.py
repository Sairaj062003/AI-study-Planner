from langchain_core.prompts import ChatPromptTemplate


request_parser_prompt = ChatPromptTemplate.from_template(
    """
    You are a study request parser.

    Convert the student's natural-language study request
    into structured information.

    Student request:
    {user_request}

    Extract the following:

    1. Available study hours.
    2. Subjects the student wants to study.
    3. Student level.

    If the student does not mention their level,
    use Beginner.

    Also identify important priorities, preferences,
    deadlines, or reasons.

    For example:

    "Python is more important because I have an interview
    next week."

    should be captured as a priority.

    Return only the structured information.
    """
)


planner_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI study planner.

    Create a practical and realistic study plan.

    Available study time:
    {hours} hours

    Subjects:
    {subjects}

    Student level:
    {level}

    Student priorities:
    {priorities}

    Previous feedback:
    {feedback}

    Instructions:

    1. Include every requested subject.
    2. Do not exceed the available study time.
    3. Consider the student's priorities.
    4. Assign High, Medium, or Low priority.
    5. Give more time to important subjects when appropriate.
    6. Create a realistic plan for the student's level.
    """
)


critic_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI study plan reviewer.

    Review the following study plan.

    Available study time:
    {hours} hours

    Requested subjects:
    {subjects}

    Student level:
    {level}

    Student priorities:
    {priorities}

    Study plan:
    {plan}

    Check:

    1. Does the total study time fit within the available time?
    2. Are all requested subjects included?
    3. Is the plan appropriate for the student's level?
    4. Is the time distribution reasonable?
    5. Does the plan respect the student's priorities?

    If the plan is reasonable:

    status = GOOD

    If the plan needs improvement:

    status = IMPROVE

    Provide a short explanation in feedback.
    """
)