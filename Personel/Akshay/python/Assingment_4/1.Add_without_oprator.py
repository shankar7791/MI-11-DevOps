#addition of two numbers without using "+" oprator

import operator
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(f"Addition of two number without using '+' operator is {operator.add(a,b)}" )