from math import factorial
x = int(input("enter the number : "))
for i in range(x):
    for j in range(x-i+1):
        print(end=" ")
  
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
  
    print()