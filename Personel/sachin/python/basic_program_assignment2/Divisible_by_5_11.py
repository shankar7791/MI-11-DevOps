number = int(input("Enter a number : "))
if number % 5 == 0 :
    if number % 11 == 0 :
        print(f"Number {number} is Divisible by 5 and 11")
    else :
        print(f"Number {number} is Divisible by 5 but not by 11")
else :
    if number % 11 == 0 :
        print(f"Number {number} is Divisible by 11 but not by 5")
    else :
        print(f"Number {number} is not Divisible by 5 and 11")