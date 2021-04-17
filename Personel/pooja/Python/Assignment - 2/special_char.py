ch = input("Enter The Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Character ", ch, "is a Digit")
else:
    print("The Character ", ch, "is a Special Character")