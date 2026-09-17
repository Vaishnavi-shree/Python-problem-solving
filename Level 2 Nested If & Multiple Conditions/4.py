# 1. Take three sides and check if they form a valid triangle.

def is_valid_triangle(a, b, c):
    # Check if the sum of any two sides is greater than the third side
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False

# Test cases
print(is_valid_triangle(7, 10, 5))  # Returns True (Valid)
print(is_valid_triangle(1, 10, 2))  # Returns False (Invalid)