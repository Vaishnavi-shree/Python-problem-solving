# Check if a given year is a leap year

year = int(input("Enter year"))
if (year % 4 == 0) and (year % 100 != 0):
    print("year is a Leap year")
else:
    print("year is not a leap year")

