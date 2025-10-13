# Start with a balance of 0
balance = 0.0

print("🏦 Welcome to Python Bank!")
print("Available actions: deposit, withdraw, balance, quit\n")

while True:
    # Ask for the user's action
    action = input("Enter an action (deposit / withdraw / balance / quit): ").lower()

    # Option to exit the program
    if action == "quit":
        print("👋 Thank you for using Python Bank. Goodbye!")
        break

    # Deposit money into the account
    elif action == "deposit":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"✅ You deposited {amount:.2f} leva.")
        else:
            print("❌ Invalid amount. Please enter a positive number.")
        # Withdraw money from the account
    elif action == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"💸 You withdrew {amount:.2f} leva.")
        elif amount > balance:
            print("⚠️ Insufficient funds.")
        else:
            print("❌ Invalid amount.")
        # Check the current balance
    elif action == "balance":
        print(f"💰 Your current balance is: {balance:.2f} leva.")

        # Handle invalid commands
    else:
        print("❌ Invalid command. Please choose: deposit, withdraw, balance, or quit.")

    print("-" * 40)  # Divider for readability

