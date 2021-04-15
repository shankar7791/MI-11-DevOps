a = int(input("enter the required number : "))
if a % 5 == 0:
    if a % 11 == 0:
        print("the number is divisible by 5 and 11 ")
    else :
        print("the number is divisible by 5 but not by 11 ")
else :
    if a % 11 == 0:
        print("the number is divisible by 11 but not 5 ")
    else :
        print("the number is neither divisible by 11 nor 5 ")