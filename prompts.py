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

    Previous study history:
    {memory_context}
    
    Memory insights:
    {memory_insights}

    Current retry reason:
    {retry_reason}

    Previous evaluation feedback:
    {feedback}
     
    If a retry reason exists:

    1. Identify the specific problem.
    2. Correct that problem.
    3. Use relevant memory when useful.
    4. Do not introduce unrelated changes.

    If previous study history is available:

    1. Learn from the student's previous sessions.
    2. Consider subjects that were previously skipped.
    3. Consider subjects that were successfully completed.
    4. Avoid repeating previous planning mistakes.
    5. Use previous history as context, not as a strict rule.
    6. Always prioritize the user's current request.

    If no previous study history exists,
    create the plan normally.

    Instructions:

    1. Include every requested subject.
    2. Do not exceed the available study time.
    3. Consider the student's priorities.
    4. Assign High, Medium, or Low priority.
    5. Give more time to important subjects when appropriate.
    6. Create a realistic plan for the student's level.
    
       when regenerating a plan:

1. Fix the issues identified by the evaluator.
2. Consider relevant historical memory.
3. Consider learned patterns from previous sessions.
4. Do not blindly repeat a previous allocation.
5. Always prioritize the user's current request.
6. Memory is supporting context, not a strict rule.

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

    Historical study memory:
    {memory_context}

    Learned memory patterns:
    {memory_insights}

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


    6. Memory Consistency

    Evaluate whether the generated plan appropriately uses the provided
    historical study memory and learned patterns.

    Consider:

    1. Does the plan learn from relevant previous study sessions?
    2. Does it consider previously skipped or completed subjects?
    3. Does it avoid blindly repeating previous mistakes?
    4. Does it avoid allowing old memory to override the user's current request?
    5. If there is no relevant memory, does the plan avoid inventing memory-based decisions?

    Give a score from 1 to 10.

    10 = memory is used appropriately and current user request remains the highest priority.
    1 = memory is ignored completely when relevant, or memory incorrectly overrides the current request.


    Scoring:

    Give every dimension an integer score from 1 to 10:
    - time_fit_score
    - subject_coverage_score
    - priority_alignment_score
    - level_suitability_score
    - realism_score
    - memory_consistency_score

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