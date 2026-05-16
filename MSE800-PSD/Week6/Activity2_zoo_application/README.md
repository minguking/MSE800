# Zoo Application - Admin Login with Decorator

A simple zoo management system with admin login, built using Python decorators.

## Project Structure

```
Activity2_zoo_application/
├── main.py         # Entry point
├── admin.py        # Admin functions (login, add/remove animal, logout)
└── decorators.py   # Decorators: log_activity, login_required
```

## Functionality

- Admin logs in by entering a username and password (`admin` / `admin123`)
- Only a logged-in admin can add or remove animals
- Every function call is automatically logged with a timestamp

## How the Decorators Work

**`log_activity`** — wraps a function to print its name, timestamp, and start/end status every time it's called.

**`login_required`** — checks if `admin_logged_in` is `True` before running the function. If not logged in, access is denied.

```python
@login_required
@log_activity
def add_animal(name, species):
    print(f"Added {name} the {species} to the zoo.")
```

Both decorators are stacked, so each protected function is both access-controlled and logged.
