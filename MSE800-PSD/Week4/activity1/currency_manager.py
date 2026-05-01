from database import create_connection
import sqlite3

def add_currency(currency_code, currency_name, country):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO currencies (currency_code, currency_name, country) VALUES (?, ?, ?)", (currency_code, currency_name, country))
        conn.commit()
        print(" Currency added successfully.")
    except sqlite3.IntegrityError:
        print(" Currency code must be unique.")
    conn.close()

def view_currencies():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM currencies")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_currency(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM currencies WHERE currency_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_currency(currency_code):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM currencies WHERE currency_code = ?", (currency_code,))
    conn.commit()
    conn.close()
    print("🗑️ Currency deleted.")
