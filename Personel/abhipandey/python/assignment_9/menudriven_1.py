

print("Enter A :")
a = int(input())
print("\nEnter B :")
b = int(input())


print("\nChoose Options To Perform : ")
print("\n1.Addition")
print("\n2.Subtraction")
print("\n3.Modulus")
print("\n4.division")
print("\n5.Multiplication")
print("\n6.Exponent")
print("\n\nEnter Your Choice :")


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
	print("\nAddition of A + B is : ",add())
elif choice==2 :
	print("\nSubtraction of A - B is : ",sub())
elif choice==3 :	
	print("\nmodulus of A * B is : ",mod())
elif choice==4 :
    print("\n division of A / B is : " , div())
    if(b == 0) :
    	print("b cannot be 0(Zero) for Division operation")
 
elif choice==5 :
    print("\n multiplication of A * b is : " , mul())
elif choice==6 :
    print("\n exponent of A**B is : " , exp())
elif choice==7 :
    print("\n wrong choice :-( ")
