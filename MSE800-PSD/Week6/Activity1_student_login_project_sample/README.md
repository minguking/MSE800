# Week 6 - Activity 1: Student Login Project

## What This Project Does

A simple student login system that uses a Python **decorator** to automatically log every student action.

---

## How the Decorator Works

`log_activity` in `decorators.py` wraps a function to print its name, timestamp, and start/end status — without changing the original function.

```python
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")
```

When `student_login("Mohammad")` is called, the flow is:
1. Print function name + timestamp
2. Print "Activity started..."
3. Run the original function
4. Print "Activity completed."

---

## Debugging: Errors Found

| File | Error | Fix |
|------|-------|-----|
| All files | No syntax errors found | Code runs successfully |

Running `python3 main.py` produced the expected output with no errors. The `wrapper(*args, **kwargs)` pattern correctly passes arguments to all three functions regardless of how many parameters they take.

---

## Findings

- One decorator (`log_activity`) handles logging for all three functions — no duplicated code.
- `*args, **kwargs` makes the decorator reusable for any function regardless of its parameters.
- Decorators separate logging logic from business logic (DRY principle).
