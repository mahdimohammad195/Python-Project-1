from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    if not User.is_valid_email(email):
        print("Email is invalid! User not created.\n")
        return

    user = User(name, email)
    users.append(user)
    print(f"User '{name}' created successfully.\n")

def list_users():
    if not users:
        print("No users found.\n")
        return
    print("\nUsers:")
    for i, user in enumerate(users):
        print(f"{i + 1}. {user}")

def select_user():
    list_users()
    if not users:
        return None
    try:
        idx = int(input("\nSelect user number: ")) - 1
        if 0 <= idx < len(users):
            return users[idx]
        print("Invalid user selected.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")
    return None

def create_account():
    user = select_user()
    if not user:
        return

    print("\nAccount Type:")
    print("1. Savings Account")
    print("2. Student Account")
    print("3. Current Account")

    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.\n")
        return

    if amount < 0:
        print("Initial deposit cannot be negative.\n")
        return

    if account_choice == 1:
        account = SavingsAccount(user.name, user.email, amount)
    elif account_choice == 2:
        account = StudentAccount(user.name, user.email, amount)
    elif account_choice == 3:
        account = CurrentAccount(user.name, user.email, amount)
    else:
        print("Invalid choice. Account not created.\n")
        return

    user.add_account(account)
    print(f"{account.get_account_type()} created and added for user '{user.name}'.\n")

def deposit_money():
    user = select_user()
    if not user:
        return

    if not user.accounts:
        print("This user has no accounts.\n")
        return

    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance():.2f}")

    try:
        acc_idx = int(input("Select account number: ")) - 1
        amount = float(input("Enter amount to deposit: "))
        if 0 <= acc_idx < len(user.accounts):
            user.accounts[acc_idx].deposit(amount)
            print(f"Rs. {amount} deposited. New Balance: Rs. {user.accounts[acc_idx].get_balance():.2f}\n")
        else:
            print("Invalid account selection.\n")
    except ValueError:
        print("Invalid input.\n")

def withdraw_money():
    user = select_user()
    if not user:
        return

    if not user.accounts:
        print("This user has no accounts.\n")
        return

    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance():.2f}")

    try:
        acc_idx = int(input("Select account number: ")) - 1
        amount = float(input("Enter amount to withdraw: "))
        if 0 <= acc_idx < len(user.accounts):
            user.accounts[acc_idx].withdraw(amount)
            print(f"Rs. {amount} withdrawn. New Balance: Rs. {user.accounts[acc_idx].get_balance():.2f}\n")
        else:
            print("Invalid account selection.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    user = select_user()
    if not user:
        return

    if not user.accounts:
        print("This user has no accounts.\n")
        return

    for i, acc in enumerate(user.accounts):
        print(f"\n{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance():.2f}")
        txs = acc.get_transaction_history()
        if not txs:
            print("No transactions.")
        else:
            for tx in txs:
                print(tx)
    print()
