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

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("um must be greater than 0")
        if amount > self.balance:
            raise ValueError("NONE")
        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= amount

    def print_transaction_history(self):
        if not self.transactions:
            print("none transaction")
        else:
            for transaction in self.transactions:
                print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder}, Balance: {self.balance}"

    def __add__(self, amount: float):
        self.deposit(amount)
        return self

    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self

