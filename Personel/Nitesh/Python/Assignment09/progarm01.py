print("Enter First Number:")
a = int(input())
print("Enter Second Number:")
b = int(input())


print("\Choose Options To Perform : ")
print("1.Addition.")
print("2.Subtraction.")
print("3.Modulus.")
print("4.division.")
print("5.Multiplication.")
print("6.Exponent.")
print("Enter The Choice:")


def add():
    c = a+b 
    return c 

def sub():
    c = a-b 
    return c

def mod():
    c = a%b
    return c

def div():
    c = a/b
    return c

def mul():
    c = a*b
    return c

def exp():
    c = a**b
    return c

 
choice = int(input())
if choice==1 :
	print("Addition of A + B is: ",add())
elif choice==2 :
	print("Subtraction of A - B is: ",sub())
elif choice==3 :	
	print("modulus of A * B is: ",mod())
elif choice==4 :
    print(" division of A / B is: " , div())
    if(b == 0) :
    	print("b cannot be 0(Zero) for Division operation")
 
elif choice==5 :
    print(" multiplication of A * b is: " , mul())
elif choice==6 :
    print(" exponent of A**B is: " , exp())
elif choice==7 :
    print(" wrong choice:-( ")