import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check the guess
if guess == secret_number:
    print("Correct! You guessed the number!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")

# Reveal the secret number
print(f"The secret number was: {secret_number}")