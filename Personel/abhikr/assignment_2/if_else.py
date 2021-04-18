#1. If statement
#2. If ...else statement
#3. Nested If statement
#4. If ...elif ...else statement
#5. shorthand If
#6. shorthand If...else


while True:
    print("""
     1. If statement.
     2. If ...else statement.
     3. Nested If statement.
     4. If ...elif ...else statement.
     5. shorthand If.
     6. shorthand If...else.
     7. Exit 
     """)

     co = int(input("Enter the choice no: "))
     
     if co==1:
         print("\n Cheaking If statement")
         x=int(input("Enter a no: ")
         if x>20:
             print("No is greater than 20")



     elif co==2:
         print("\n Checking if else statement")
         x=int(input("Enter a no: "))
         if x%2==0:
             print("no is even ")
             else:
                 print("no is odd: ")


     elif co==3:
         print("\n Cheaking Nested if else statement")
         x=int(input("Enter a no: "))
         if x%2==0:
             if x%3==0:
                 print("no is divisible by 6 ")
             else :
                 print("no is not divisible by 6 ")
         else:
             print("no is not divisible by 6 ")   


    elif co==4:
        print("\n Checking if else ladder statement ")
          x=int(input("Enter a no: "))
          if x<20:
          print("no is less than 20")
          elif x>30:
              print("no is greater than 30")
          else:
             print("no lies between 20 and 30")


    elif co==5:
        print("\n Checking shorthand if ")  
        x=int(input("Enter a no: "))
        if x>10:print("no is greater than 10")       
    

    elif  co==6:
        print("\n Checking shorthand if ..else statement")
        x=int(input("Enter your  age: "))
        if x>=18: print("valid for vote") else:print("Invalid ofr vote")

    elif co==7:
        exit    
