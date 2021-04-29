def recfac(a):
    if a == 1:
        return a
    else:
        return a * recfac(a-1)
num = int(input("enter a number : "))
if num < 0:
    print("enter positive number.")
elif num == 0 :
    print(" factorial of 0 is 1.")
else:
    print("factorial of number", num , "=" , recfac(num))