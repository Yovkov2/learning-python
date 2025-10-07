# Ask the user to choose a conversion type
choice = input("Convert from (C)elsius or (F)ahrenheit? ").lower()

# Convert from Celsius to Fahrenheit
if choice == "c":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C = {fahrenheit}°F")
# Convert from Fahrenheit to Celsius
elif choice == "f":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")

else:
    print("Invalid choice. Please enter 'C' or 'F'.")