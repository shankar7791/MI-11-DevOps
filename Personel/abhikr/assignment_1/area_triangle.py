#prog 1.3.Python Program to calculate area of Triangle
a =int(input("Enter the number "))
b =int(input("Enter the number "))
c =int(input("Enter the number "))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is',area)