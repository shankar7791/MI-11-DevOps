def check_vowel(stri) :
    stri = stri.lower()
    vowels = set("aeiou")
    s = set({})

    for i in stri :
        
        if i in vowels :
            s.add(i)
        else :
            pass
    
    if len(s) == len(vowels) :
        print("\nString is accepted. ")
    else :
        print("\nString is not accepted. ")
    
stri = input("Enter a String : ")
check_vowel(stri)