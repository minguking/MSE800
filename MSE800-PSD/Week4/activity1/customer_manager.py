from database import create_connection
import sqlite3

def add_customer(name, email, phone, nationality, date_of_birth):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers (name, email, phone, nationality, date_of_birth) VALUES (?, ?, ?, ?, ?)", (name, email, phone, nationality, date_of_birth))
        conn.commit()
        print(" Customer added successfully.")
    except sqlite3.IntegrityError:
        print(" Email and phone must be unique.")
    conn.close()

def view_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_customer(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_customer(customer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    conn.close()
    print("🗑️ Customer deleted.")

