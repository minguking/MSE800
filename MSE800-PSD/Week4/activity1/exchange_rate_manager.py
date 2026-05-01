from database import create_connection
import sqlite3

def add_exchange_rate(from_currency, to_currency, rate):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES (?, ?, ?)", (from_currency, to_currency, rate))
        conn.commit()
        print(" Exchange rate added successfully.")
    except sqlite3.IntegrityError:
        print(" Exchange rate for this currency pair already exists.")
    conn.close()

def view_exchange_rates():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exchange_rates")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_exchange_rate(from_currency, to_currency):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exchange_rates WHERE from_currency = ? AND to_currency = ?", (from_currency, to_currency))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_exchange_rate(from_currency, to_currency):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM exchange_rates WHERE from_currency = ? AND to_currency = ?", (from_currency, to_currency))
    conn.commit()
    conn.close()
    print("🗑️ Exchange rate deleted.")
