# If the sides from a valid triangle, determine whether it is equilateral, isosceles, or scalene

def classify_triangle(a, b, c):
    """
    Checks if three sides form a valid triangle and determines its type:
    Equilateral, Isosceles, or Scalene.
    """
    # 1. Check for triangle validity (Triangle Inequality Theorem)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid Triangle: The sides do not form a valid triangle."
    
    # 2. Check for negative or zero lengths
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Triangle: Side lengths must be greater than zero."

    # 3. Determine the triangle type
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# --- Test Cases ---
print(classify_triangle(5, 5, 5))  # Output: Equilateral Triangle
print(classify_triangle(5, 5, 8))  # Output: Isosceles Triangle
print(classify_triangle(3, 4, 5))  # Output: Scalene Triangle
print(classify_triangle(1, 2, 5))  # Output: Invalid Triangle



