while True :
    print(""" 
    1.)If statement
    2.)If-else statement
    3.)nested If-else statement
    4.)If-elif ladder
    5.)shorthand if
    6.)return
    """)

    option = int(input("Enter the choice:"))

    if option == 1:
        print("if statement")
        x = int(input("enter a number: "))
        if x > 20 :
            print("number is greater than 20")

    elif option == 2:
        print("if-else statement")
        a =  int(input("enter the number: "))
        if a < 50 :
            print("a is less than 50 ")
        else:
            print("a is greater than 50 ")

    elif option == 3:
        print("nested if-else ")
        b = int(input("enter the number of choice :"))
        if b%4 == 0 :
            if b%5 == 0 :
                print("Number is Divisible by 5")
            else :
                print("Number is not Divisible by 5")
        else :
            print("Number is not Divisible by 4")

    elif option == 4:
        print("if - elif ladder ")
        c = int(input("enter the number: "))
        if c <=15:
            print("age is less than 15 , eligible")
        elif c >= 35 :
            print("age is greater than 35 , elegible")
        else :
            print("not eligible")

    elif option == 5:
        print("shorthand if ")
        e = int(input("enter the age: "))
        if e > 18 : print("eligible for driving liscense: ")

    elif option == 6:
        break

    else : 
        print ("invalid choice , bye bye ")
        break

        

