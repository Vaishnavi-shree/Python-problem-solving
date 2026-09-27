# Take a 4-digit number and check if the first and last digits are equal.

num = input("Enter a four digit no.")

if len(num) == 4 and num.isdigit():

    first = int(num[0])
    last = int(num[3])

    if first == last :
        print("First and last digit are equal")
else:
    print("not equal")


