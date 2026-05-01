
# Finance Money Exchange System

A command-line banking and currency exchange management system built with Python and SQLite.

## How to Run

```bash
python main.py
```

## Database Tables

This system uses **5 tables**, each representing a core entity in the money exchange domain.

---

### 1. `currencies`
Stores information about currencies supported by the system.

**Why it's necessary:** Every financial transaction and account must be denominated in a specific currency. This table acts as the foundation for the entire system — accounts and exchange rates both reference it to ensure only valid, recognised currencies are used.

---

### 2. `customers`
Stores personal details of registered customers.

**Why it's necessary:** A banking system must identify who owns what. Customer records hold identity information (name, email, phone, nationality, date of birth) and are linked to accounts, making it possible to trace financial activity back to a real person.

---

### 3. `accounts`
Stores bank accounts belonging to customers, each denominated in a currency.

**Why it's necessary:** An account is the primary financial container — it holds a balance and links a customer to a currency. Separating accounts from customers also allows one customer to hold multiple accounts in different currencies, which is essential in a money exchange context.

---

### 4. `exchange_rates`
Stores buy, sell, and mid rates for each currency.

**Why it's necessary:** Currency exchange requires three distinct rate values (buy, sell, mid) to reflect real-world market conditions. Storing these separately from the currency table allows rates to be updated independently without affecting the currency records themselves.

---

### 5. `transactions`
Records financial transactions made through accounts.

**Why it's necessary:** A money exchange system must maintain a full audit trail of all financial movements. This table captures the what, when, and how much of every transaction, which is critical for accountability, reporting, and debugging financial discrepancies.

---

## Project Structure

| File | Description |
|---|---|
| `database.py` | Creates DB connection and initialises all tables |
| `main.py` | Entry point — main menu and sub-menu navigation |
| `currency_manager.py` | CRUD operations for currencies |
| `customer_manager.py` | CRUD operations for customers |
| `account_manager.py` | CRUD operations for accounts |
| `exchange_rate_manager.py` | CRUD operations for exchange rates |
| `transaction_manager.py` | CRUD operations for transactions |
