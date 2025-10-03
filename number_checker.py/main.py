# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is greater than 100
if number > 100:
    print("Big number")

# Check if the number is between 50 and 100 (inclusive)
elif number >= 50 and number <= 100:
    print("Medium number")

# If neither of the above conditions is true → number is less than 50
else:
    print("Small number")
