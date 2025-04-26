from account.transaction import Transaction
from account.user import User

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Invalid initial balance!")
            return  # Prevents further initialization if the balance is invalid
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.user = User(name, email)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount is invalid!")
            return
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return
        if self.balance < amount:
            print("Insufficient Balance!")
            return
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user


class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print(f"Cannot withdraw! A minimum balance of Rs.{self.MIN_BALANCE} must remain in your account.")
            return
        super().withdraw(amount)

    def get_account_type(self):
        return "Savings account"


class CurrentAccount(BankAccount):
    def get_account_type(self):
        return "Current account"


class StudentAccount(BankAccount):
    def withdraw(self, amount):
        if (self.balance - amount) < 100:
            print("A minimum balance of Rs.100 needed to withdraw from a Student's account!")
            return
        super().withdraw(amount)

    def get_account_type(self):
        return "Student's account"


