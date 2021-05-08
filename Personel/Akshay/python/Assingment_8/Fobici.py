
def recur(n):
    if n <= 1:
       return n
    else:
       return(recur(n-1) + recur(n-2))

n = int(input("Enter a Number : "))
if n <= 0:
   print("Cannot generate Fibbonaci Series for Negative integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recur(i))