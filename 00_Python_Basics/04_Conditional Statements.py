a = int(input("Enter first a number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third mumber:"))

if a >= b and a >= c:
    print("greatest number is:", a)
elif b >= a and b >= c:
    print("greatest number is:", b)
else:
    print("greatest number is :", c)
