data = input("Enter a Character : ")
if data.isdigit() == True :
    print("Enetered Character is Digit")
elif data.isalpha() == True :
    print("Entered Character is Alphabet")
else :
    print("Entered Character is Special Character")