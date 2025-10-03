# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check if the person is an adult (between 18 and 65 inclusive)
if age >= 18 and age <= 65:
    print("Adult")

# If the age is less than 18 → Child
elif age < 18:
    print("Child")

# If the age is greater than 65 → Senior
elif age > 65:
    print("Senior")
