
import random

# Create a list with the possible options
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to stop playing.\n")

# Start an infinite loop for the game
while True:
    # Ask the user for their choice
    user_choice = input("Your choice: ").lower()

    # Option to quit the game
    if user_choice == "quit":
        print("Thanks for playing! Goodbye! 👋")
        break

    # Validate user input
    if user_choice not in choices:
        print("❌ Invalid choice. Please type rock, paper, or scissors.")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    # Compare choices to determine the result
    if user_choice == computer_choice:
        print("It's a tie! 😐")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    print("-" * 30)  # Divider for readability
