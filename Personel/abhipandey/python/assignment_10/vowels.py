def check(string):
    string = string.replace(" " , " ")
    string = string.lower()
    vowel = [string.count('a') , string.count('e') , string.count('i') , string.count('o') , string.count('u')]
    if vowel.count(0) > 0:
        return("not vowel.")
    else:
        return("vowel")
string = input("enter the string :")
print(check(string))
        