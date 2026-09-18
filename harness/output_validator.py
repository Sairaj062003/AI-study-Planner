from state import StudyState

def validate_plan(state: StudyState):
    """
    Deterministically validate the generated plan.
    """

    plan = state["plan"]

    

    if plan is None:
        return {
            "validation_status": "IMPROVE",
            "feedback": "No study plan was generated."
        }

     # --------------------------------
    # Rule 1: Get requested subjects
    # --------------------------------

    requested_subjects = {
        subject.strip().lower()
        for subject in state["subjects"].split(",")
        if subject.strip()
    }


    # --------------------------------
    # Rule 2: Get plan subjects
    # --------------------------------

    plan_subjects = [
        item.subject.strip().lower()
        for item in plan.items
    ]


    # --------------------------------
    # Rule 3: Check for duplicate subjects
    # --------------------------------

    if len(plan_subjects) != len(set(plan_subjects)):

        print("Plan validation failed.")

        return {
            "validation_status": "IMPROVE",
            "feedback": (
                "The study plan contains duplicate subjects. "
                "Each subject should appear only once."
            )
        }


    # --------------------------------
    # Rule 4: Check for missing subjects
    # --------------------------------

    missing_subjects = (
        requested_subjects - set(plan_subjects)
    )

    if missing_subjects:

        print("Plan validation failed.")

        return {
            "validation_status": "IMPROVE",
            "feedback": (
                "The study plan is missing these subjects: "
                + ", ".join(sorted(missing_subjects))
            )
        }


    # --------------------------------
    # Rule 5: Check for unexpected subjects
    # --------------------------------

    unexpected_subjects = (
        set(plan_subjects) - requested_subjects
    )

    if unexpected_subjects:

        print("Plan validation failed.")

        return {
            "validation_status": "IMPROVE",
            "feedback": (
                "The study plan contains unexpected subjects: "
                + ", ".join(sorted(unexpected_subjects))
            )
        }    
    
    # --------------------------------
    # Rule 6: Check total hours
    # --------------------------------
    total_hours = sum(
        item.hours
        for item in plan.items
    )

    available_hours = state["hours"]

    # Check total study time
    if total_hours > available_hours:

        print("Plan validation failed.")

        return {
            "validation_status": "IMPROVE",
            "feedback": (
                f"The plan uses {total_hours} hours, "
                f"but only {available_hours} hours "
                "are available. Reduce the study time."
            )
        }

    # 7 Check for negative or zero hours
    for item in plan.items:

        if item.hours <= 0:

            print("Plan validation failed.")

            return {
                "validation_status": "IMPROVE",
                "feedback": (
                    f"{item.subject} has an invalid "
                    "study duration."
                )
            }

    # --------------------------------
    # Rule 8: Check priorities
    # --------------------------------

    valid_priorities = {
        "high",
        "medium",
        "low"
    }


    for item in plan.items:

        if item.priority.strip().lower() not in valid_priorities:

            print("Plan validation failed.")

            return {
                "validation_status": "IMPROVE",
                "feedback": (
                    f"{item.subject} has an invalid priority "
                    f"'{item.priority}'. Priority must be "
                    "High, Medium, or Low."
                )
            }


    # --------------------------------
    # Everything passed
    # --------------------------------        

    print("Plan validation passed.")

    return {
        "validation_status": "VALID",
        "feedback": ""
    }
