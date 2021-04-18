
#2.Python program to check Leap year

x=int(input("Enter a year "))
if (x % 4) == 0:
   if (x% 100) == 0:
       if (x% 400) == 0:
           print("{0} is a leap year".format(x))
       else:
           print("{0} is not a leap year".format(x))
   else:
       print("{0} is a leap year".format(x))
else:
   print("{0} is not a leap year".format(x))

