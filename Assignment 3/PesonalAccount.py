from datetime import datetime


class Amount:
    def __init__(self, value: float, transaction_type: str, ):
        self.value = value
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.transaction_type}: {self.value} (date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("sum of the deposit must be greater of 0")
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount
