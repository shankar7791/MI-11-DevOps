print("\nChoose the Given Option : ")
print("\n1.Addition")
print("\n2.Subtraction")
print("\n3.Modulus")
print("\n4.Division")
print("\n5.Multiplication")
print("\n6.Exponent")
print("\nEnter Your Choice :")


def add():
    c = a + b 
    return c 

def sub():
    c = a - b 
    return c

def mod():
    c = a % b
    return c

def div():
    c = a / b
    return c

def mul():
    c = a * b
    return c

def exp():
    c = a ** b
    return c

    
choice = int(input())
a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))

if choice==1 :
	print("\nAddition is = ",add())
elif choice==2 :
	print("\nSubtraction is = ",sub())
elif choice==3 :	
	print("\nModulus is = ",mod())
elif choice==4 :
    print("\nDivision is = " , div())
elif choice==5 :
    print("\n multiplication is = " , mul())
elif choice==6 :
    print("\n exponent is =" , exp())
elif choice==7 :
    print("\n wrong choice : ")