from decorators import log_activity


# @log_activity wraps student_login — every call is automatically logged without changing its logic
@log_activity
def student_login(username):
    # prints a login confirmation message for the given student
    print(f"{username} logged into the system.")


# @log_activity wraps submit_assignment — reuses the same decorator without duplicating log code
@log_activity
def submit_assignment(username, assignment):
    # prints which student submitted which assignment
    print(f"{username} submitted {assignment}.")


# @log_activity wraps view_grades — all three functions share one decorator for consistent logging
@log_activity
def view_grades(username):
    # prints which student is viewing their grades
    print(f"{username} is viewing grades.")
