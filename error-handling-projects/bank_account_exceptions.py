class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"✅ {self.owner} deposited {amount:.2f} leva. New balance: {self.balance:.2f} leva.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(f"❌ Not enough funds! Available: {self.balance:.2f} leva.")
        self.balance -= amount
        print(f"💸 {self.owner} withdrew {amount:.2f} leva. Remaining balance: {self.balance:.2f} leva.")

    def __str__(self):
        """Return a readable string representation of the account."""
        return f"🏦 Account owner: {self.owner} | Balance: {self.balance:.2f} leva"


if __name__ == "__main__":
    print("Welcome to Python Bank!\n")

    # Create an account
    account = BankAccount("Ivan", 100.0)
    print(account)
    print("-" * 40)

    try:
        # Valid deposit
        account.deposit(50)

        # Valid withdrawal
        account.withdraw(30)

        # Invalid withdrawal (custom exception)
        account.withdraw(200)

    except ValueError as ve:
        print(f"⚠️ Input Error: {ve}")

    except InsufficientFundsError as ife:
        print(f"⚠️ Transaction Error: {ife}")

    finally:
        print("\n✅ Transaction process complete.")
        print(account)