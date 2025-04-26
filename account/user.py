import re

class User:
    EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    def __init__(self, name, email):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email address: {email}")

        self.name = name.strip()
        self.email = email.strip()
        self.accounts = []

    def add_account(self, account):
        if account not in self.accounts:
            self.accounts.append(account)
        else:
            raise ValueError("Account already added for this user.")

    def get_total_balance(self): 
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Account '{account.get_account_type()}' removed successfully."
        else:
            raise ValueError("Account not found for this user.")

    @classmethod
    def is_valid_email(cls, email):
        if isinstance(email, str) and re.match(cls.EMAIL_REGEX, email):
            return True
        return False

    def __str__(self):
        return (f"{self.name} ({self.email}) - "
                f"{self.get_account_count()} account(s), "
                f"Total Balance: ${self.get_total_balance():.2f}")
