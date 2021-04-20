vowels = ['a','e','i','o','u','A','E','I','O','U']
a = input("Enter a Character : ")
for i in vowels :
    if i == a :
        print ("Entered Character is a Vowel")
        break
else :
    print ("Entered Character is consonant")