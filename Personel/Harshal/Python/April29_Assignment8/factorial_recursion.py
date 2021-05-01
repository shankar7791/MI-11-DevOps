def fact(n) :
    if n == 1 :
        return n
    else :
        return n * fact(n-1)

val = int(input("Enter a number : "))

if val == 0 :
    print("Factorial of 0 is 1")
elif val < 0 :
    print("Factorial Does not Exist ")
else :
    print(f"Factorial of {val} is {fact(val)}")