# Loop through numbers from 1 to 20
for number in range(1, 21):

    # Skip numbers that are divisible by 3
    if number % 3 == 0:
        continue

    # Stop the loop when number is 15
    if number == 15:
        break

    # Print the current number
    print(number)
