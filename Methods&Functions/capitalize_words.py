# Define a function that capitalizes the first letter of each word in a sentence
def capitalize_words(sentence):
    # Use the built-in .title() method to capitalize the first letter of every word

    formatted_sentence = sentence.title()

    # Return the formatted text
    return formatted_sentence
# Example function call
text = "python is fun and powerful"
print(capitalize_words(text))  # Output: "Python Is Fun And Powerful"