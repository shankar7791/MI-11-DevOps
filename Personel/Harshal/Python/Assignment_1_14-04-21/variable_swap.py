a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(f"Berfore Swapping First Number is {a} and Second Number is {b}")
c = a           #a = a + b , b = a - b
a = b
b = c
print(f"After Swapping First Number is {a} and Second Number is {b}")