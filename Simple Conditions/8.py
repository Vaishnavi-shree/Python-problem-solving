# Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions

temp = int(input("Enter temp value in celsius"))
if temp >= 100 :
    print("hot")
elif 50<temp<100 :
    print("warm")
else:
    print("Cold")