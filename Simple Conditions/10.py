# Take a character and check whether it’s uppercase, lowercase, a digit, or a special character.

def check_character_type(ch):
    # Check if the character is an uppercase letter
    if 'A' <= ch <= 'Z':
        return "Uppercase Letter"
    
    # Check if the character is a lowercase letter
    elif 'a' <= ch <= 'z':
        return "Lowercase Letter"
    
    # Check if the character is a digit
    elif '0' <= ch <= '9':
        return "Digit"
    
    # If it doesn't match any of the above, it's a special character
    else:
        return "Special Character"

# Example usage:
user_input = input("Enter a single character: ")
if len(user_input) == 1:
    print(f"'{user_input}' is a {check_character_type(user_input)}")
else:
    print("Please enter exactly one character.")
