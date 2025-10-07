# Define a function that returns all even numbers from a given list
def get_even_numbers(numbers):
    # Create an empty list to store even numbers
    even_numbers = []
    # Loop through all numbers in the list
    for num in numbers:
        # Check if the number is even using the modulo operator (%)
        if num % 2 == 0:
            # Add the even number to the new list
            even_numbers.append(num)

    # Return the list of even numbers
    return even_numbers
# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(nums))  # Output: [2, 4, 6, 8, 10]
