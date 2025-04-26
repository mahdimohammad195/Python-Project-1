from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from bank_operator import bank_operator  # Ensure this module has necessary functions like create_user, list_users, etc.

console = Console()

def menu():
    while True:
        # Clear the console screen
        console.clear()

        # Create and style the menu table
        table = Table(title="🏦 Bank System Menu", title_style="bold magenta")
        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        # Add rows to the menu
        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "Deposit")
        table.add_row("5", "Withdraw")
        table.add_row("6", "View Transactions")
        table.add_row("7", "Exit")

        # Print the table
        console.print(table)

        # Ask user for a choice
        choice = Prompt.ask("👉 Choose an option", choices=[str(i) for i in range(1, 8)], default="7")

        # Handle user choices
        if choice == '1':
            bank_operator.create_user()  # Assumes create_user() exists in bank_operator
        elif choice == '2':
            bank_operator.list_users()  # Assumes list_users() exists in bank_operator
        elif choice == '3':
            bank_operator.create_account()  # Assumes create_account() exists in bank_operator
        elif choice == '4':
            bank_operator.deposit_money()  # Assumes deposit_money() exists in bank_operator
        elif choice == '5':
            bank_operator.withdraw_money()  # Assumes withdraw_money() exists in bank_operator
        elif choice == '6':
            bank_operator.view_transactions()  # Assumes view_transactions() exists in bank_operator
        elif choice == '7':
            console.print("\n👋 Exiting... Thank you for using the Bank System!", style="bold green")
            break  # Exit the loop

if __name__ == "__main__":
    menu()
