#check vowel
vowels = ['a','e','i','o','u']
a = input("Enter a Character : ")
a = a.lower()
for i in vowels :
    if i == a :
        print ("Entered Character is a Vowel")
        break
else :
    print ("Entered Character is consonant")
