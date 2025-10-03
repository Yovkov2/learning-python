# Create a dictionary for a student
student = {"name": "Anna", "age": 17, "grades": [5, 6, 4, 6]}

# Print the student's name
print("Name:", student["name"])

# Get the list of grades
grades = student["grades"]

# Calculate the average grade
average = sum(grades) / len(grades)
print("Average grade:", average)

# Check performance
if average > 5:
    print("Excellent")
else:
    print("Needs improvement")
