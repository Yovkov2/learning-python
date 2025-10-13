import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Start an infinite loop until the user guesses correctly
while True:
    # Ask the user to enter a number
    guess = int(input("Enter your guess: "))

    # Increase the attempt counter
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break  # Exit the loop when guessed correctly

    # Give hints if the guess is too low or too high
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
