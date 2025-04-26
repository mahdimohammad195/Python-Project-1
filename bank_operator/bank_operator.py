from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    # Validate the email before creating the user
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid! User not created.")
        return  # Exit the function if email is invalid
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users found.")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    list_users()
    idx = int(input("Select user number: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user selected.")
        return

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    account_choice = int(input("Enter your choice (1, 2, 3): "))
    amount = float(input("Enter initial deposit: "))

    # Creating accounts based on type selection
    if account_choice == 1:
        account = SavingsAccount(users[idx].name, users[idx].email, amount)
    elif account_choice == 2:
        account = StudentAccount(users[idx].name, users[idx].email, amount)
    elif account_choice == 3:
        account = CurrentAccount(users[idx].name, users[idx].email, amount)
    else:
        print("Invalid choice! Defaulting to generic bank account.")
        account = BankAccount(users[idx].name, users[idx].email, amount)

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user selected.")
        return

    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    
    acc_idx = int(input("Select account: ")) - 1
    if acc_idx < 0 or acc_idx >= len(user.accounts):
        print("Invalid account selected.")
        return

    amount = float(input("Enter amount to deposit: "))  # Fixed bug
    user.accounts[acc_idx].deposit(amount)
    print(f"Deposited Rs. {amount}. New Balance: Rs. {user.accounts[acc_idx].get_balance()}\n")

def withdraw_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user selected.")
        return

    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    
    acc_idx = int(input("Select account: ")) - 1
    if acc_idx < 0 or acc_idx >= len(user.accounts):
        print("Invalid account selected.")
        return

    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        print(f"Withdrawal successful. New Balance: Rs. {user.accounts[acc_idx].get_balance()}\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user selected.")
        return

    user = users[idx]
    if not user.accounts:
        print("No accounts found for this user.")
        return

    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        transactions = acc.get_transaction_history()
        if not transactions:
            print("No transactions found.")
        for tx in transactions:
            print(tx)
