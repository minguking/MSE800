from users import (
    student_login,
    submit_assignment,
    view_grades
)


# Entry point: runs three student actions to demonstrate the decorator in action
def main():

    # each call below triggers log_activity automatically via the @log_activity decorator
    student_login("Mohammad")               # test: login event

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"          # test: assignment submission event
    )

    view_grades("Alex")                     # test: grade-viewing event


if __name__ == "__main__":
    main()
