import sqlite3

def create_connection():
    conn = sqlite3.connect("banking.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor() # mandatory
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currencies(
            currency_code TEXT PRIMARY KEY,
            currency_name TEXT NOT NULL,
            country TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            nationality TEXT NOT NULL,
            date_of_birth TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number TEXT NOT NULL UNIQUE,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL,
            customer_id INTEGER,
            currency_code TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (currency_code) REFERENCES currencies(currency_code)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            buy_rate REAL NOT NULL,
            sell_rate REAL NOT NULL,
            mid_rate REAL NOT NULL,
            currency_code TEXT NOT NULL,
            FOREIGN KEY (currency_code) REFERENCES currencies(currency_code)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            fee REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
