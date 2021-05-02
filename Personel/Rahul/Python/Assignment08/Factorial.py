def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input("Enter Number : "))

if num < 0:
   print("Enter positive number")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The Factorial Is", recur_factorial(num))


