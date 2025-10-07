# Define a function to calculate the area of different shapes
def calculate_area(shape,a, b = 0):
    # Convert shape name to lowercase to avoid case sensitivity issues
    shape = shape.lower()

    # If the shape is a rectangle → area = a * b
    if shape == "rectangle":
        return  a * b
    # If the shape is a triangle → area = (a * b) / 2
    elif shape == "triangle":
        return  (a * b) / 2
    # If the shape is a square → area = a ** 2
    elif shape == "square":
        return  a ** 2
    # If an unknown shape is provided
    else:
        return "Unknown shape"
    
# Example function calls
print(calculate_area("rectangle", 5, 3))
print(calculate_area("triangle", 6, 4))
print(calculate_area("square", 5))