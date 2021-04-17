#div by 5 or 11
i = int(input("Enter a number : "))
if i % 5 == 0 :
    if i % 11 == 0 :
        print(f"Number {i} is Divisible by 5 and 11 ")
    else :
        print(f"Number {i} is Divisible by 5 but not by 11")
else :
    if i % 11 == 0 :
        print(f"Number {i} is Divisible by 11 but not by 5")
    else :
        print(f"Number {i} is not Divisible by 5 and 11")  

