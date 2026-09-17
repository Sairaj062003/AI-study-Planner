from graph import graph

def get_hours():
    while True:
        try:
            hours = float(input("How many hours do you have today? "))

            if hours <= 0:
                print("Please enter a number greater than 0.")
                continue

            if hours > 24:
                print("You cannot study more than 24 hours in a day.")
                continue

            return hours

        except ValueError:
            print("Please enter a valid number.")


def get_subjects():
    while True:
        subjects = input(
            "What subjects do you want to study? "
        ).strip()

        if subjects:
            return subjects

        print("Please enter at least one subject.")


def get_level():
    valid_levels = {
        "beginner": "Beginner",
        "intermediate": "Intermediate",
        "advanced": "Advanced"
    }

    while True:
        level = input(
            "What is your level? "
            "(Beginner/Intermediate/Advanced) "
        ).strip().lower()

        if level in valid_levels:
            return valid_levels[level]

        print(
            "Please enter Beginner, Intermediate, or Advanced."
        )


print("========== AI STUDY PLANNER ==========")

hours = get_hours()
subjects = get_subjects()
level = get_level()


initial_state = {
    "hours": hours,
    "subjects": subjects,
    "level": level,
    "plan": None,
    "feedback": "",
    "review_status": None,
    "attempt": 0
}

def display_plan(result):
    plan = result["plan"]

    print("\n========== YOUR STUDY PLAN ==========")

    total_hours = 0

    for index, item in enumerate(plan.items, start=1):
        print(f"\n{index}. {item.subject}")
        print(f"   Time: {item.hours} hours")
        print(f"   Priority: {item.priority}")

        total_hours += item.hours

    print("\n-------------------------------------")
    print(f"Total study time: {total_hours} hours")
    print(f"Attempts: {result['attempt']}")
    print("-------------------------------------")

result = graph.invoke(initial_state)




display_plan(result)



