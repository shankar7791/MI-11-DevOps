while True :
    print(""" 
    1.)If statement
    2.)If-else statement
    3.)nested If-else statement
    4.)If-elif ladder
    5.)shorthand if
    6.)return
    """)

    opt = int(input("Enter the choice:"))

    if opt == 1:
        print("if statement")
        x = int(input("enter a number: "))
        if x > 20 :
            print("number is greater than 20")

    elif opt == 2:
        print("if-else statement")
        a =  int(input("enter the number: "))
        if a < 50 :
            print("a is less than 50 ")
        else:
            print("a is greater than 50 ")

    elif opt == 3:
        print("nested if-else ")
        b = int(input("enter the marks of student :"))
        if b >=90:
            print("congratulations")
            if b < 35:
                print ("failed")
            if b > 35:
                print("no worries passed ") 
            if b < 70 :
                print(" well done student")
        else :
            print ("marks entered invalid")

    elif opt == 4:
        print("if - elif ladder ")
        c = int(input("enter the number: "))
        if c <=15:
            print("age is less than 15 , eligible")
        elif c >= 35 :
            print("age is greater than 35 , elegible")
        else :
            print("not eligible")

    elif opt == 5:
        print("shorthand if ")
        e = int(input("enter the age: "))
        if e > 18 : print("eligible for driving liscense: ")

    elif opt == 6:
        break

    else : 
        print ("invalid choice , bye bye ")

        

