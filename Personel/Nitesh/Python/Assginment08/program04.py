def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = int(input("Enter Number :"))

if num < 0:
   print("")
else:
   print("The sum of sequence of all number is :",recur_sum(num))