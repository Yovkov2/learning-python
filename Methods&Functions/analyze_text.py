# Define a function that analyzes a given text
def analyze_text(text):
    # Remove extra spaces and split the text into words

    words = text.split()
    # Count total number of words
    total_words = len(words)

    # Count total number of letters (excluding spaces)
    letters_only = [ch for ch in text if ch.isalpha()]
    total_letters = len(letters_only)

    # Create a dictionary to store how many times each word appears
    word_count = {}

    # Loop through each word in the list
    for word in words:
        # Capitalize the first letter for consistent counting
        formatted = word.capitalize()

        # Add word to dictionary or increase its count
        if formatted in word_count:
            word_count[formatted] += 1
        else:
            word_count[formatted] = 1

    # Return all results in a single dictionary
    return {
        "letters": total_letters,
        "words": total_words,
        "word_count": word_count
    }


# Example usage
sample_text = "Python is fun and Python is powerful"
result = analyze_text(sample_text)

# Display the analysis in a readable format
print(f"Letters: {result['letters']}")
print(f"Words: {result['words']}")
print(f"Word count: {result['word_count']}")