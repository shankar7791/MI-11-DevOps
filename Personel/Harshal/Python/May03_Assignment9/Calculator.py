import operator

def add():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    print(f"\nAddition of two number is {operator.add(a,b)}" )

def sub():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    print(f"\nSubtraction of two number is {operator.sub(a,b)}" )

def mod():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    print(f"\nModulus of two number is {operator.mod(a,b)}" )

def div():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    if b == 0:
        print("\nCannot Divide by zero")
    else :
        print(f"\nDivision of two number is {operator.truediv(a,b)}" )

def mul():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    print(f"\nMultiplication of two number is {operator.mul(a,b)}" )

def exp():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    print(f"\nExponent of first number to second number is {operator.pow(a,b)}" )

while True:
    print("""
    1.Addition
    2.Subtraction
    3.Modulus
    4.Division
    5.Multiplication
    6.Exponent
    7.Exit """)
    
    print()
    
    ch = int(input("Enter your Choice : "))
    
    if ch == 1 :
        add()
    
    elif ch == 2 :
        sub()

    elif ch == 3 :
        mod()

    elif ch == 4 :
        div()

    elif ch == 5 :
        mul()

    elif ch == 6 :
        exp()
    
    elif ch == 7 :
        exit()
    
    else :
        print("\nWrong Choice")