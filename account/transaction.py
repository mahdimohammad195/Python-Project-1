from datetime import datetime

class Transaction:
    VALID_TYPES = {"deposit", "withdraw"}  # Set for faster lookup

    def __init__(self, amount, transaction_type):
        # Validate amount
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        
        # Validate transaction type
        if not isinstance(transaction_type, str):
            raise TypeError("Transaction type must be a string.")
        transaction_type = transaction_type.lower()
        if transaction_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid transaction type. Must be one of {', '.join(self.VALID_TYPES)}.")
        
        # Assign attributes
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: ${self.amount:.2f}"

# Example Usage
if __name__ == "__main__":
    try:
        t1 = Transaction(100, "deposit")
        print(t1)
        t2 = Transaction(50, "withdraw")
        print(t2)
        t3 = Transaction(-10, "deposit")  # This will raise an exception
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")