def safe_division():
    print("Welcome to the Safe Division Calculator!")

    try:
        # Ask for user input
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Try to perform the division
        result = numerator / denominator

    except ZeroDivisionError:
        print("❌ Error: You cannot divide by zero.")

    except ValueError:
        print("❌ Error: Please enter valid numbers only.")

    else:
        # Only runs if no exception occurred
        print(f"✅ Result: {numerator} ÷ {denominator} = {result:.2f}")

    finally:
        # Always runs at the end
        print("Thank you for using the Safe Division Calculator.\n")

if __name__ == "__main__":
    safe_division()