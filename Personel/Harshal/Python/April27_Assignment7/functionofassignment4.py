import operator
from datetime import datetime as dt


def add():
    a = int(input("\nEnter first number : "))
    b = int(input("\nEnter second number : "))
    print(f"\nAddition of two number without using '+' operator is {operator.add(a,b)}" )


def bmi():
    height = float(input("\nInput your height : "))
    weight = float(input("\nInput your weight : "))
    bmi = round(weight / (height ** 2), 2)
    print(f"\nYour BMI is: {bmi}")


def ti_me(): 
    now = dt.now().time()
    print(f"\nCurrent Time is {now} ")


def palindrome():
    def rev_number(n):
        num = 0
        while True:
            val = str(n)
            if val == val[::-1]:
                break
            else:
                rev = int(val[::-1])
                n += rev
                num += 1
        return n 

    num = int(input("\nEnter a Number : "))
    final = rev_number(num)
    print(f"\nPallindrome number is {final}")


def triangle():
    side1 = float(input("\nEnter the first side of a triangle : "))
    side2 = float(input("\nEnter the second side of a triangle : "))
    side3 = ((side1 ** 2) + (side2 ** 2)) ** 0.5
    print(f"\nThe Third side of Right angled Triangle is : {side3}")

while True:
    print("""
    1.Addition
    2.BMI
    3.Current Time
    4.Pallindrome
    5.Third Side of Triangle
    6.Exit """)
    ch = int(input("/nEnter your Choice : "))
    if ch == 1 :
        add()
    
    elif ch == 2 :
        bmi()

    elif ch == 3 :
        ti_me()

    elif ch == 4 :
        palindrome()

    elif ch == 5 :
        triangle()

    elif ch == 6 :
        exit()
 