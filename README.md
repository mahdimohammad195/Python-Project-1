# account/bank_account.py
from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if transaction_type not in ("deposit", "withdraw"):
            raise ValueError("Transaction type must be 'deposit' or 'withdraw'.")
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: ${self.amount:.2f}"

class BankAccount:
    def __init__(self, name, email, initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.name = name
        self.email = email
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.balance < amount:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def __str__(self):
        return f"{self.account_type} Account - {self.name} ({self.email}) | Balance: ${self.get_balance():.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self.account_type = "Savings"

class CurrentAccount(BankAccount):
    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self.account_type = "Current"

class StudentAccount(BankAccount):
    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self.account_type = "Student"