
    print("""
    1. If Statement
    2. if-else statement
    3. Nested-if
    4. if-elif-ladder
    5. Shorthand if
    6. Shorthand if-else
    7. Exit
    """)

    opt = int(input("Enter The Choice Number: "))


    if opt == 1 :
        print("\n Check if Statement")
        i = 20 
        if(i>25):
           print("20 is less than 25")
        print("True")    
        
            
    elif opt == 2 :
        print("\n Check if-else Statement")
        i = 20 
        if(i<15):
           print(" i is smaller than 15")
           print("True")  
        else:
            print(" i is greater than 15")
            print("False")   
        print("True False")


    elif opt == 3 :
        num = 10 
        if num > 5 :
           print("Bigger than 5")
           
           if num <= 15:
              print("Between 5 and 15")


    elif opt == 4 :
        print("\n Check if-elif-else-ladder Statement")
        i = 20
        if (i == 5):
            print("i is 5")
        elif (i == 10) :
            print("i is 10")
        else :
            print(" i is not present")


    elif opt == 5 :
        print("\n Check Shorthand if Statement")
        i = 15
        if i < 15 : print("i is less than 15")


    elif opt == 6 :
        print("\n Check Shorthand if-else Statement")
        i = 10
        print("True") if i < 15 else print("False")


    elif opt == 7 :
        break


    else :
        print("\n No Choice")
