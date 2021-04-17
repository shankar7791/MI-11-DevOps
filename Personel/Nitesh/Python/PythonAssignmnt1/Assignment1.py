# Q1.Python Program to Add two numbers.

# Adding two number or float value
var1 = 13.5
var2 = 12.5

#Adding the two given numbers
sum = float(var1) + float(var2)


#Displaying the addition result
print("The sum of the given numbers is:", sum)


# Q2. Python Program to find Square root of number.

number = int(input("enter a number: "))
sqrt = number ** 0.5
print("square root:", sqrt)

# Q3.Python Program to calculate area of Triangle.

a = float(input("Please enter the first side of triangle:"))
b = float(input("Please enter the second side of triangle:"))
c = float(input("Please enter the third side of triangle:"))

# calculate the Perimeter
Perimeter = a + b + c

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("\n The Perimeter of Traiangle = %.2f" %Perimeter)
print(" The Semi Perimeter of Traiangle = %.2f" %s)
print(" The Area of a Triangle is %.2f" %Area)

#Q4.Python Program to swap two variables.


x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

#Q5.Python Program to genrate random number.

import random

print(random.randint(0,9))

# Q6. Python Program to Convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))