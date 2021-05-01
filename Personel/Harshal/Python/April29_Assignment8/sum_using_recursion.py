def recur(n) :
    if n <= 1 :
        return n
    else :
        return n + recur(n-1)

val = int(input("Enter a Number : "))

if val < 0 :
    print("Enter a Positive Number.")
else :
    print(f"Sum of sequence of number upto {val} is {recur(val)}")