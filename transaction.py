from datetime import datetime


class Transaction:

    VALID_TYPE = ("deposit", "withdrawal")

    def __init__(self, transaction_id: str, transaction_type: str,
                 account_no: str, amount: float, timestamp: str = None):
        if transaction_type not in self.VALID_TYPE:
            raise ValueError(f"Invalid trasaction type: '{transaction_type}'\n"
                             f"Please choose from: {self.VALID_TYPE}")
        if amount <= 0:
            raise ValueError("Amout must be greater than 0")

        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.account_no = account_no
        self.amount = amount
        self.timestamp = timestamp or datetime.now()

    def get_summary(self) -> str:
        direction = "+" if self.transaction_type == "deposit" else "-"
        return (f"[{self.timestamp}] {self.transaction_id} "
                f"{self.transaction_type}: {direction}€{self.amount} "
                f"on account: {self.account_no}")

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "account_no": self.account_no,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }

    def __str__(self) -> str:
        return self.get_summary()
