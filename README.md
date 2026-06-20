# Banking-System-Python
Final project: Computer programming with Python

# ManoBank — Simple Retail Bank System

A command-line retail banking application built in Python as part of the
B100 Introduction to Computer Programming module at GISMA University of
Applied Sciences.

---

## Purpose

ManoBank simulates core operations of a retail bank: registering customers,
opening accounts, depositing and withdrawing funds, and viewing transaction
history. All data is persisted between sessions using CSV files.

---

## Key Features

- Register and manage bank customers
- Open savings or current accounts
- Deposit and withdraw funds with full validation
- View transaction history per account
- Persistent storage via CSV files (no database required)
- Graceful error handling (invalid amounts, missing accounts, etc.)
- Modular codebase — one class per file

---

## File Structure

```
bank_system/
├── main.py           # Entry point — menu-driven CLI
├── bank.py           # Bank class — orchestrates all operations
├── customer.py       # Customer class
├── account.py        # Account class + InsufficientFundsError
├── transaction.py    # Transaction class
├── file_manager.py   # CSV read/write for all entities
├── data/
│   ├── customers.csv      # Auto-generated on first run
│   ├── accounts.csv       # Auto-generated on first run
│   └── transactions.csv   # Auto-generated on first run
└── README.md
```

---

## Requirements

- Python 3.8 or higher
- No external packages required (uses only the standard library)

---

## Installation & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/OusmaneMano/Banking-System-Python.git
   cd Banking-System-Python/bank_system
   ```

2. Run the application:
   ```bash
   python main.py
   ```

The `data/` directory and CSV files are created automatically on first run.

---

## Example Usage

```
  Welcome to ManoBank!

─────────────────────────────────────────────
  ManoBank — Main Menu
─────────────────────────────────────────────
  1. Register new customer
  2. List all customers
  3. Open new account
  ...
  0. Exit

  Enter choice: 1

─────────────────────────────────────────────
  Register New Customer
─────────────────────────────────────────────
  Full name   : Ousmane Traore
  Email       : ousmane@example.com
  Phone       : +491777967944

  ✔ Customer registered successfully.
  ID: C3F8A12B | Name: Ousmane Traore | Email: ousmane@example.com | Phone: +491777967944
```

---

## Error Handling Examples

- Withdrawing more than the available balance raises `InsufficientFundsError`
- Entering a non-numeric amount is caught with a `ValueError` and re-prompted
- Looking up a non-existent customer or account raises `KeyError` with a clear message
