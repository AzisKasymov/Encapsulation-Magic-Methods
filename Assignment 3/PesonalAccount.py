from datetime import datetime


class Amount:
    def __init__(self, value: float, transaction_type: str, ):
        self.value = value
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.transaction_type}: {self.value} (Дата: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"