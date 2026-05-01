from database import create_connection
import sqlite3

def add_transaction(account_id, amount, transaction_type, currency_code, timestamp):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO transactions (account_id, amount, transaction_type, currency_code, timestamp) VALUES (?, ?, ?, ?, ?)", (account_id, amount, transaction_type, currency_code, timestamp))
        conn.commit()
        print(" Transaction added successfully.")
    except sqlite3.IntegrityError:
        print(" Failed to add transaction. Check account ID and currency code.")
    conn.close()

def view_transactions():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_transaction(account_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE account_id = ?", (account_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_transaction(transaction_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    print("🗑️ Transaction deleted.")
