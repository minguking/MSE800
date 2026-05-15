from datetime import datetime


# Decorator: wraps any function to automatically log its name, timestamp, and start/end status
def log_activity(func):

    # wrapper accepts the same arguments as the original function
    def wrapper(*args, **kwargs):
        print("===================================")
        print(f"Function: {func.__name__}")   # shows which function is being called
        print(f"Time: {datetime.now()}")       # records when the activity happens
        print("Activity started...")

        result = func(*args, **kwargs)         # calls the original function

        print("Activity completed.")
        print("===================================\n")

        return result                          # returns the original function's result

    return wrapper  # returns wrapper so it replaces the decorated function
