# Take a 3-digit number and check if all digits are distinct.

def has_distinct_digits(number):
    # Convert the number to a string to access individual characters
    num_str = str(number)
    
    # Compare the length of the string to the length of its set
    return len(num_str) == len(set(num_str))

# Test cases
print(has_distinct_digits(123))  # Returns True (1, 2, and 3 are unique)
print(has_distinct_digits(122))  # Returns False (2 is repeated)
print(has_distinct_digits(404))  # Returns False (4 is repeated)


