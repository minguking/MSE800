from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from currency_manager import add_currency, view_currencies, search_currency, delete_currency
from customer_manager import add_customer, view_customers, search_customer, delete_customer
from account_manager import add_account, view_accounts, search_account, delete_account
from exchange_rate_manager import add_exchange_rate, view_exchange_rates, search_exchange_rate, delete_exchange_rate
from transaction_manager import add_transaction, view_transactions, search_transaction, delete_transaction

## Main Menu
def menu():
    print("\n==== Banking Manager ====")
    print("1. Currency Management")
    print("2. Customer Management")
    print("3. Account Management")
    print("4. Exchange Rate Management")
    print("5. Transaction Management")
    print("6. Exit")

## Sub Menus
def currency_management_menu():
    print("\n==== Currency Management ====")
    print("1. Add Currency")
    print("2. View Currencies")
    print("3. Search Currency")
    print("4. Delete Currency")
    print("5. Back to Main Menu")

def customer_management_menu():
    print("\n==== Customer Management ====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Delete Customer")
    print("5. Back to Main Menu")

def account_management_menu():
    print("\n==== Account Management ====")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Back to Main Menu")

def exchange_rate_management_menu():
    print("\n==== Exchange Rate Management ====")
    print("1. Add Exchange Rate")
    print("2. View Exchange Rates")
    print("3. Search Exchange Rate")
    print("4. Delete Exchange Rate")
    print("5. Back to Main Menu")

def transaction_management_menu():
    print("\n==== Transaction Management ====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Search Transaction")
    print("4. Delete Transaction")
    print("5. Back to Main Menu")


def handle_currency():
    while True:
        currency_management_menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            currency_code = input("Enter Currency Code: ")
            currency_name = input("Enter Currency Name: ")
            country = input("Enter Country: ")
            add_currency(currency_code, currency_name, country)
        elif choice == '2':
            # View currencies logic
            currencies = view_currencies()
            for currency in currencies:
                print(currency)
        elif choice == '3':
            # Search currency logic
            currency_name = input("Enter Currency Name to search: ")
            currencies = search_currency(currency_name)
            for currency in currencies:
                print(currency)
        elif choice == '4':
            # Delete currency logic
            currency_code = input("Enter Currency Code to delete: ")
            delete_currency(currency_code)
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

def handle_customer():
    while True:
        customer_management_menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            phone = input("Enter Customer Phone: ")
            nationality = input("Enter Customer Nationality: ")
            date_of_birth = input("Enter Customer Date of Birth (DD-MM-YYYY): ")
            add_customer(name, email, phone, nationality, date_of_birth)
        elif choice == '2':
            # View customers logic
            customers = view_customers()
            for customer in customers:
                print(customer)
        elif choice == '3':
            # Search customer logic
            name = input("Enter Customer Name to search: ")
            customers = search_customer(name)
            for customer in customers:
                print(customer)
        elif choice == '4':
            # Delete customer logic
            customer_id = int(input("Enter Customer ID to delete: "))
            delete_customer(customer_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")
            
def handle_account():
    while True:
        account_management_menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            account_number = input("Enter Account Number: ")
            account_type = input("Enter Account Type (Savings/Checking): ")
            balance = float(input("Enter Initial Balance: "))
            customer_id = int(input("Enter Customer ID: "))
            currency_code = input("Enter Currency Code: ")
            add_account(account_number, account_type, balance, customer_id, currency_code)
        elif choice == '2':
            # View accounts logic
            accounts = view_accounts()
            for account in accounts:
                print(account)
        elif choice == '3':
            # Search account logic
            account_number = input("Enter Account Number to search: ")
            accounts = search_account(account_number)
            for account in accounts:
                print(account)
        elif choice == '4':
            # Delete account logic
            account_number = input("Enter Account Number to delete: ")
            delete_account(account_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

def handle_exchange_rate():
    while True:
        exchange_rate_management_menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            buy_rate = float(input("Enter Buy Rate: "))
            sell_rate = float(input("Enter Sell Rate: "))
            mid_rate = float(input("Enter Mid Rate: "))
            currency_code = input("Enter Currency Code: ")
            add_exchange_rate(buy_rate, sell_rate, mid_rate, currency_code)
        elif choice == '2':
            # View exchange rates logic
            exchange_rates = view_exchange_rates()
            for rate in exchange_rates:
                print(rate)
        elif choice == '3':
            # Search exchange rate logic
            currency_code = input("Enter Currency Code to search: ")
            exchange_rates = search_exchange_rate(currency_code)
            for rate in exchange_rates:
                print(rate)
        elif choice == '4':
            # Delete exchange rate logic
            currency_code = input("Enter Currency Code to delete: ")
            delete_exchange_rate(currency_code)
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

def handle_transaction():
    while True:
        transaction_management_menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            account_id = int(input("Enter Account ID: "))
            amount = float(input("Enter Transaction Amount: "))
            transaction_type = input("Enter Transaction Type (Deposit/Withdrawal): ")
            currency_code = input("Enter Currency Code: ")
            timestamp = input("Enter Timestamp (YYYY-MM-DD HH:MM:SS): ")
            add_transaction(account_id, amount, transaction_type, currency_code, timestamp)
        elif choice == '2':
            # View transactions logic
            transactions = view_transactions()
            for transaction in transactions:
                print(transaction)
        elif choice == '3':
            # Search transaction logic
            account_id = int(input("Enter Account ID to search: "))
            transactions = search_transaction(account_id)
            for transaction in transactions:
                print(transaction)
        elif choice == '4':
            # Delete transaction logic
            transaction_id = int(input("Enter Transaction ID to delete: "))
            delete_transaction(transaction_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

def main(): 
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            handle_currency()
        elif choice == '2':
            handle_customer()
        elif choice == '3':
            handle_account()
        elif choice == '4':
            handle_exchange_rate()
        elif choice == '5':
            handle_transaction()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\n======== BYE! ========\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")