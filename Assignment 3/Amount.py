from datetime import datetime

class Amount:
    def __init__(self, value: float, currency: str, timestamp: datetime = None):
        self.value = value
        self.currency = currency
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"{self.value} {self.currency} (create: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"

    def add(self, other):
        if self.currency != other.currency:
            raise ValueError("NONE")
        return Amount(self.value + other.value, self.currency)


a1 = Amount(100, "USD")
a2 = Amount(50, "USD")
a3 = a1.add(a2)

print(a1)
