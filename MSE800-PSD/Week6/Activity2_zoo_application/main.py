from admin import (
    admin_login,
    add_animal,
    remove_animal,
    admin_logout
)


# Entry point: runs three student actions to demonstrate the decorator in action
def main():

    # each call below triggers log_activity automatically via the @log_activity decorator
    username = input("Username: ")
    password = input("Password: ")
    admin_login(username, password)          # test: login event

    add_animal("Leo", "Lion")              # test: adding an animal

    remove_animal("Leo", "Lion")           # test: removing an animal

    admin_logout("mingu")                   # test: logout event


if __name__ == "__main__":
    main()
