while True :
    print("""
    1.)If Statement
    2.)If Else statement
    3.)Nested If
    4.)If-elif ladder
    5.)Shorthand if
    6.)Shorthand if-else
    7.)Exit
    """)

    opt = int(input("Enter The Choice Number: "))


    if opt == 1 :
        print("\n Checking If Statement")
        x = int(input("Enter A Number: "))
        if x > 25 :
            print("Number is Greater Than 25")


    elif opt == 2 :
        print("\n Checking If else Statement")
        x = int(input("Enter A Number: "))
        if x%2 == 0 :
            print("Number is Even")
        else :
            print("Number is Odd")


    elif opt == 3 :
        print("\n Checking Nested If else Statement")
        x = int(input("Enter A Number: "))
        if x%2 == 0 :
            if x%3 == 0 :
                print("Number is Divisible by 12")
            else :
                print("Number is not Divisible by 12")
        else :
            print("Number is not Divisible by 12")


    elif opt == 4 :
        print("\n Checking If elif Ladder Statement")
        x = int(input("Enter A Number: "))
        if x > 20 :
            print("Number is Greater than 20")
        elif x < 10:
            print("Number is less than 10")
        else :
            print("Number is Between 10 and 20")


    elif opt == 5 :
        print("\n Checking Shorthand If Statement")
        x = int(input("Enter A Number: "))
        if x > 10 : print("Number is Greater than 10")


    elif opt == 6 :
        print("\n Checking Shorthand If else Statement")
        x = int(input("Enter your Age: "))
        print("Valid for Voting") if x >= 18 else print("Not eligible for Voting")


    elif opt == 7 :
        break


    else :
        print("\n Wrong Entry")