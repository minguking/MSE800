from database import create_connection
import sqlite3

def add_account(account_number, account_type, balance, customer_id, currency_code):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO accounts (account_number, account_type, balance, customer_id, currency_code) VALUES (?, ?, ?, ?, ?)", (account_number, account_type, balance, customer_id, currency_code))
        conn.commit()
        print(" Account added successfully.")
    except sqlite3.IntegrityError:
        print(" Account number must be unique.")
    conn.close()

def view_accounts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_account(account_number):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE account_number LIKE ?", ('%' + account_number + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_account(account_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    conn.commit()
    conn.close()
    print("🗑️ Account deleted.")

