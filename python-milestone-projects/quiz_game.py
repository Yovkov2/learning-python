# ----------------------------------------
# 🧠 Quiz Game
# ----------------------------------------
# A simple quiz application where the player answers
# multiple-choice questions and receives a score at the end.
# ----------------------------------------

# Create a dictionary with questions and answers
# Each key is a question, and its value is the correct answer (A, B, or C)
questions = {
    "What is the capital of France?": "A",
    "Which language is used for web development?": "B",
    "What is 5 * 3?": "C",
    "Who created Python?": "A",
    "Which planet is known as the Red Planet?": "C"
}

# Create a dictionary with the multiple-choice options
options = {
    "What is the capital of France?": ["A. Paris", "B. Rome", "C. Berlin"],
    "Which language is used for web development?": ["A. C++", "B. JavaScript", "C. Swift"],
    "What is 5 * 3?": ["A. 10", "B. 20", "C. 15"],
    "Who created Python?": ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates"],
    "Which planet is known as the Red Planet?": ["A. Earth", "B. Venus", "C. Mars"]
}

# Initialize the score counter
score = 0

print("🎓 Welcome to the Python Quiz Game!")
print("Type A, B, or C for your answers.\n")

# Loop through each question in the dictionary
for question in questions:
    print(question)  # Print the question text

    # Print the options for this question
    for option in options[question]:
        print(option)

    # Get the user's answer
    answer = input("Your answer: ").upper()

    # Check if the answer is correct
    if answer == questions[question]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {questions[question]}.\n")

# Display final score after the quiz ends
print(f"🏁 Quiz finished! You scored {score} out of {len(questions)}.")
