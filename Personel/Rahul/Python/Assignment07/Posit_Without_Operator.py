a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
def add(a,b):   
    while(b != 0):
        c=a&b 
        a=a^b 
        b=c<<1 
    return a
print("Sum of two numbers:",add(a, b))