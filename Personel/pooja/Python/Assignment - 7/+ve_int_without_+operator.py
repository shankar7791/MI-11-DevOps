a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
def add(a,b):   
    while(b != 0):
        c=a&b 
        a=a^b 
        b=c<<1 
    return a
    
    
print("Sum of two numbers",add(a, b))