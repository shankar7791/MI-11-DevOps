#prog 4.1.Write a Python program to add two positive integers
#  without using the '+' operator.

x=int(input("Enter input one: "))

y=int(input("Enter input two: "))

def addition_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
    
print(addition_without_plus_operator(x,y))