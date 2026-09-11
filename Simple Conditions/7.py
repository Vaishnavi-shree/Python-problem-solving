# Take three numbers and print the largest

num1 = float(input("Enter num1"))
num2 = float(input("Enter num2"))
num3 = float(input("Enter num3"))

if num1>num2 and num2>num3 :
    print(num1)
elif num2>num1 and num1>num3 :
    print(num2)
else:
    print(num3)
