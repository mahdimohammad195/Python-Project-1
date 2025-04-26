import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import bank_operator  # Must contain the required functions

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
        clear_screen()

        # Create menu table
        table = Table(title="🏦 Bank System Menu", title_style="bold magenta")
        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        # Menu options
        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "Deposit")
        table.add_row("5", "Withdraw")
        table.add_row("6", "View Transactions")
        table.add_row("7", "Exit")

        console.print(table)

        # Get user choice
        choice = Prompt.ask("👉 Choose an option", choices=[str(i) for i in range(1, 8)], default="7")

        try:
            if choice == '1':
                bank_operator.create_user()
            elif choice == '2':
                bank_operator.list_users()
            elif choice == '3':
                bank_operator.create_account()
            elif choice == '4':
                bank_operator.deposit_money()
            elif choice == '5':
                bank_operator.withdraw_money()
            elif choice == '6':
                bank_operator.view_transactions()
            elif choice == '7':
                console.print("\n👋 Exiting... Thank you for using the Bank System!", style="bold green")
                break
        except Exception as e:
            console.print(f"[bold red]⚠️ Error:[/bold red] {str(e)}")

        input("\nPress [bold cyan]Enter[/bold cyan] to continue...")

if __name__ == "__main__":
    menu()
