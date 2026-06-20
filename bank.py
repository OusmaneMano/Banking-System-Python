
import uuid

from customer import Customer
from account import Account
from transaction import Transaction
from file_manager import FileManager

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers: dict = FileManager.load_customer()
        self.accounts: dict = FileManager.load_account()
        self.transactions: list = FileManager.load_transaction()

    def add_customer(self, name: str, email: str, phone: str) -> Customer:
        if not (name and email and phone):
            raise ValueError("Name, Email and Phone must be filled")

        customer_id = "C" + str(uuid.uuid4())[:8].upper()
        customer = Customer(customer_id, name, email, phone)
        self.customers[customer_id] = customer
        FileManager.save_customer(self.customers)
        return customer

    def find_customer(self, customer_id: str) -> Customer:
        if customer_id not in self.customers:
            raise KeyError(f"Customer: {customer_id} not found")
        return self.customers[customer_id]

    def list_customer(self) -> list:
        return list(self.customers.values())


    def open_account(self, customer_id: str, account_type: str = "saving") -> Account:
        self.find_customer(customer_id)

        account_no = "ACC" + str(uuid.uuid4())[ :8].upper()
        account = Account(account_no, customer_id, account_type)
        self.accounts[account_no] = account
        FileManager.save_account(self.accounts)
        return account

    def find_account(self, account_no) -> Account:
        if account_no not in self.accounts:
            raise ValueError(f"Account N°: {account_no} not found")
        return self.accounts[account_no]

    def get_customer_account(self, customer_id: str) -> list:
        return [acc for acc in self.accounts.values() if acc.customer_id == customer_id]

    #transaction

    def _record_transaction(self, account_no, transaction_type: str, amount: float) -> Transaction:
        transaction_id = "TXT" + str(uuid.uuid4())[:8].upper()
        transaction = Transaction(transaction_id, transaction_type, account_no, amount)
        self.transactions.append(transaction)
        FileManager.save_transaction(self.transactions)
        return transaction


    def deposit(self, account_no: str, amount: float) -> Transaction:
        account = self.find_account(account_no)
        account.deposit(amount)
        transaction = self._record_transaction(account_no, "deposit", amount)
        FileManager.save_account(self.accounts)
        return transaction

    def withdraw(self, account_no: str, amount:float) -> Transaction:
        account = self.find_account(account_no)
        account.withdrawal(amount)
        transaction = self._record_transaction(account_no, "withdrawal", amount)
        FileManager.save_account(self.accounts)
        return transaction

    def get_account_transaction(self, account_no: str) -> list:
        return [t for t in self.transactions if t.account_no == account_no]

    def get_reports(self) -> str:
        total_balance = sum(acc.balance for acc in self.accounts.values())
        lists = [f"{'*'*20}\n",
                f"Name: {self.name.upper()}\n"
                f"Customer: {len(self.customers)}\n"
                f"Account: {len(self.accounts)}\n"
                f"Transaction: {len(self.transactions)}\n"
                f"Total Deposit: €{total_balance:,.2f}\n",
                 f"{'*'*20}"]
        return "\n".join(lists)
