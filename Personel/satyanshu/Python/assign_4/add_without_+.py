#addition without using + operator
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
def add(a,b):   
    while(b != 0):
        c=a&b #and operator
        a=a^b #Xor operator
        b=c<<1 #left shift
    return a
    
    
print("Sum of two numbers",add(a,b))


