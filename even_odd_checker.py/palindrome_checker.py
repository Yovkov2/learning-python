# Ask the user to enter a word
word = input("Enter a word: ")

# Reverse the word using slicing
reversed_word = word[::-1]

# Check if it's a palindrome
if word == reversed_word:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")