import csv
import os

from customer import Customer
from account import Account
from transaction import Transaction

class FileManager:
    DATA_DIR = os.path.join(str(os.path.dirname(__file__)), "data")

    CUSTOMER_FILE = os.path.join(DATA_DIR, "customer.csv")
    ACCOUNT_FILE = os.path.join(DATA_DIR, "account.csv")
    TRANSACTION_FILE = os.path.join(DATA_DIR, "transaction.csv")

    CUSTOMER_FIELD = ["customer_id", "name", "email", "phone"]
    ACCOUNT_FIELD = ["account_no", "customer_id", "account_type", "balance"]
    TRANSACTION_FIELD = ["transaction_id","transaction_type",
                         "account_no", "amount", "timestamp"]

    @staticmethod
    def _ensure_data_dir() -> None:
        os.makedirs(FileManager.DATA_DIR, exist_ok = True)

    @staticmethod
    def save_customer(customers: dict) -> None:
        FileManager._ensure_data_dir()

        with open(FileManager.CUSTOMER_FILE, "w", newline = "", encoding = "utf-8") as f:
            writer = csv.DictWriter(f, fieldnames = FileManager.CUSTOMER_FIELD)
            writer.writeheader()
            for customer in customers.values():
                writer.writerow(customer.to_dict())

    @staticmethod
    def load_customer() -> dict:
        customers = {}
        if not os.path.exists(FileManager.CUSTOMER_FILE):
            return customers

        with open(FileManager.CUSTOMER_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                customer = Customer(
                    customer_id=row["customer_id"],
                    name=row["name"],
                    email=row["email"],
                    phone=row["phone"]
                )
                customers[customer.customer_id] = customer
        return customers

    @staticmethod
    def save_account(accounts: dict) -> None:
        FileManager._ensure_data_dir()

        with open(FileManager.ACCOUNT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames = FileManager.ACCOUNT_FIELD)
            writer.writeheader()
            for account in accounts.values():
                writer.writerow(account.to_dict())

    @staticmethod
    def load_account() -> dict:
        accounts = {}

        if not os.path.exists(FileManager.ACCOUNT_FILE):
            return accounts

        with open(FileManager.ACCOUNT_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                account = Account(
                    account_no=row["account_no"],
                    customer_id=row["customer_id"],
                    account_type=row["account_type"],
                    balance=float(row["balance"])
                )
                accounts[account.account_no] = account
        return accounts

    @staticmethod
    def save_transaction(transactions: list) -> None:
        FileManager._ensure_data_dir()
        with open(FileManager.TRANSACTION_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames = FileManager.TRANSACTION_FIELD)
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction.to_dict())

    @staticmethod
    def load_transaction() -> list:
        transactions = []

        if not os.path.exists(FileManager.TRANSACTION_FILE):
            return transactions

        with open(FileManager.TRANSACTION_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transaction = Transaction(
                    transaction_id=row["transaction_id"],
                    transaction_type=row["transaction_type"],
                    account_no =row["account_no"],
                    amount=float(row["amount"]),
                    timestamp =row["timestamp"]
                )
                transactions.append(transaction)
        return transactions
