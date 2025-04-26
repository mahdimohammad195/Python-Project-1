# account/bank_account.py
from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type  # "deposit" or "withdraw"
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: ${self.amount}"

class BankAccount:
    def __init__(self, name, email, initial_balance=0):
        self.name = name
        self.email = email
        self.balance = initial_balance
        self.transactions_history = []

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

    def __str__(self):
        return f"{self.name} ({self.email}) - Balance: ${self.get_balance()}"

class SavingsAccount(BankAccount):
    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self.account_type = "Savings"

class CurrentAccount(BankAccount):
    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self.account_type = "Current"