from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        # Ensure amount is a positive value
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        
        # Validate transaction type to be either "deposit" or "withdraw"
        valid_types = ["deposit", "withdraw"]
        if transaction_type.lower() not in valid_types:
            raise ValueError(f"Invalid transaction type. Must be one of {valid_types}.")
        
        # Normalize the transaction type to lowercase
        self.amount = amount
        self.transaction_type = transaction_type.lower()
        self.timestamp = datetime.now()

    def __str__(self):
        # Return a string in the required format
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: ${self.amount:.2f}"

# Example Usage
try:
    t1 = Transaction(100, "deposit")
    print(t1)
    t2 = Transaction(50, "withdraw")
    print(t2)
    t3 = Transaction(-10, "deposit")  # This will raise an exception
except ValueError as e:
    print(f"Error: {e}")
