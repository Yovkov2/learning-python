# Define a function that can take any number of names
def greet_multiple(*args):
    # Loop through each name passed into the function
    for name in args:
        # Print a personalized greeting for each person
        print(f"Hello, {name}!")

# Call the function with three names as arguments
(greet_multiple("Anna", "Peter", "Maria"))