def check(string):
    string = string.replace(" " , " ")
    string = string.lower()
    vowel = [string.count('a') , string.count('e') , string.count('i') , string.count('o') , string.count('u')]
    if vowel.count(0) > 0:
        return("Not Vowel.")
    else:
        return("Vowel")
string = input("Enter The String :")
print(check(string))