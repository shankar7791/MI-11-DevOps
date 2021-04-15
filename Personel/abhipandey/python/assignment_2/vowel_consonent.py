vowels = ['a' , 'e' , 'i' , 'o' , 'u']
str1 = str(input("enter the alphabet : "))
for i in vowels :
    if i == str1 :
        print("it is a vowel ")
        break
else :
    print("it is a consonent ") 