# Ask the user for a number
number = int(input())
# Initialize factorial result
factorial = 1
# Calculate factorial using a for loop
for i in range(1, number + 1):
    factorial *= i

# Display the result
print(f"The factorial of {number} is {factorial}")