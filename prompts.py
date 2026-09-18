from langchain_core.prompts import ChatPromptTemplate


request_parser_prompt = ChatPromptTemplate.from_template(
    """
    You are a study request parser.

    Convert the student's natural-language study request
    into structured information.

    Student request:
    {user_request}

    Extract:

    1. Available study hours.
    2. Subjects the student wants to study.
    3. Student level.
    4. Subject priorities.

    Level rules:

    If the student does not mention their level,
    use Beginner.

    Priority rules:

    Use High, Medium, or Low.

    If the student explicitly says that a subject is
    more important, urgent, or needed for an upcoming
    interview/exam/deadline, assign that subject High priority.

    If a subject is mentioned without any special
    importance, assign Medium priority.

    If the student explicitly says a subject is less
    important, assign Low priority.

    Every requested subject should have a priority.

    Example:

    "I have 4 hours today. I need to study Python,
    DSA and LangChain. Python is more important because
    I have an interview next week."

    should produce priorities similar to:

    Python -> High
    DSA -> Medium
    LangChain -> Medium

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

    Use these priorities when deciding how much time
    to allocate to each subject.

Previous evaluation feedback:
{feedback}

If previous evaluation feedback is provided:

1. Identify what was wrong with the previous plan.
2. Correct that issue in the new plan.
3. Do not repeat the same allocation mistake.
4. Preserve parts of the previous plan that were already good.
    """
)

evaluator_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI study plan evaluator.

    Evaluate the quality of the generated study plan.

    Important:
    Basic structural correctness has already been checked
    by deterministic Python validation.

    Focus on the QUALITY of the plan.

    Available study time:
    {hours} hours

    Requested subjects:
    {subjects}

    Student level:
    {level}

    Student priorities:
    {priorities}

    Generated study plan:
    {plan}


    Evaluate the plan using these dimensions:

    1. Time Fit

    Is the distribution of study time sensible?
    A plan can technically fit within the available hours
    but still distribute the time poorly.


    2. Subject Coverage

    Does the plan give reasonable attention to all
    requested subjects?

    Do not simply check whether subjects exist.
    Evaluate whether their allocated time is reasonable.


    3. Priority Alignment

    Does the plan give appropriate importance and time
    to high-priority subjects?

    High-priority subjects should generally receive
    more attention when appropriate.


    4. Level Suitability

    Is the plan appropriate for the student's level?


    5. Realism

    Could a real student realistically follow this plan?


    Scoring:

    Give every dimension a score from 1 to 10.

    1 = Very poor
    5 = Average
    10 = Excellent


    Important:

    Do not reject the plan only because it does not use
    every available hour.

    Focus on whether the generated plan is practical,
    sensible, and aligned with the student's request.

    Finally, provide concise overall feedback.
    """
)