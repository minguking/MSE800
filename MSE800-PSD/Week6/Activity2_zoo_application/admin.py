import decorators
from decorators import log_activity, login_required

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


@log_activity
def admin_login(username, password):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        decorators.admin_logged_in = True
        print("Admin login successful.")
    else:
        print("Invalid username or password.")

@login_required
@log_activity
def add_animal(name, species):
    print(f"Added {name} the {species} to the zoo.")

@login_required
@log_activity
def remove_animal(name, species):
    print(f"Removed {name} the {species} from the zoo.")

@login_required
@log_activity
def admin_logout(name):
    decorators.admin_logged_in = False
    print(f"{name} logged out.")
