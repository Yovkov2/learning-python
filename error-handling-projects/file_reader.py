def read_file():
    print("Welcome to the File Reader!\n")

    try:
        # Ask the user for a filename
        filename = input("Enter the name of the file to read: ")

        # Try opening the file in read mode
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

            # Check if the file is empty
            if not content.strip():
                print("⚠️ The file is empty.")
            else:
                print("\n📖 File Contents:")
                print("-" * 40)
                print(content)
                print("-" * 40)

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the file name and try again.")

    except PermissionError:
        print("❌ Error: You don't have permission to open this file.")

    except Exception as e:
        # Generic handler for unexpected errors
        print(f"⚠️ An unexpected error occurred: {e}")

    finally:
        print("📘 Thank you for using the File Reader!\n")


if __name__ == "__main__":
    read_file()