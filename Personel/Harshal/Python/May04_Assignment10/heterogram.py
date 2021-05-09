def hetro(stri) : 
    set_stri = set(stri)
    #print (inps)
    if len(set_stri)==len(stri):
        print ("Entered String is Heterogram")
    else:
        print("Entered String is not Heterogram")
        
stri = input("enter the string : ")
stri = stri.lower()
hetro(stri)