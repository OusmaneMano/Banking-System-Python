class InsufficientFondError(Exception):
    pass

class Account:
    VALID_TYPE = ("saving", "current")

    def __init__(self, account_no: str, customer_id: str,
                 account_type: str = "saving", balance: float = 0.0):

        if account_type not in self.VALID_TYPE:
            raise ValueError(f"Invalid account type:\nPlease Choose from: {self.VALID_TYPE}")

        self.account_no = account_no
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance += amount
        return self.balance

    def withdrawal(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > self.balance:
            raise InsufficientFondError("Insufficient balance")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> str:
        return f"€{self.balance:.2f}"

    def to_dict(self) -> dict:
        return {
            "account_no": self.account_no,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance,
        }

    def __str__(self):
        return (f"Account N°: {self.account_no}\nAccount Type: {self.account_type}\n"
                f"Balance: {self.get_balance()}")
