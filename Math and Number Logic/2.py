# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.

# Take a 3-digit number from the user
num_str = input("Enter a 3-digit number: ")

# Validate that the input is a 3-digit number
if len(num_str) == 3 and num_str.isdigit():
    # Extract the digits
    first = int(num_str[0])
    middle = int(num_str[1])
    last = int(num_str[2])
    
    # Compare the middle digit with the other two digits
    if middle > first and middle > last:
        print(f"The middle digit ({middle}) is the largest.")
    elif middle < first and middle < last:
        print(f"The middle digit ({middle}) is the smallest.")
    else:
        print(f"The middle digit ({middle}) is neither the largest nor the smallest.")
else:
    print("Please enter a valid 3-digit number.")
