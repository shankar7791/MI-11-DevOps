x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))
if (x >= y) and (x >= z):
   largest = x
elif (y >= x) and (y>= z):
   largest = y
else:
   largest = z
print("The largest number is", largest)

