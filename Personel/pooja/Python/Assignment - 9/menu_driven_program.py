print("\n Choose the Given Option : ")
print("\n 1.Length of String ")
print("\n 2.Reverse String")
print("\n 3.Check Palindrome or not")
print("\n 4.Check Symmetrical or not")
print("\n 5.Check Permutations and Combination")
print("\n 6.Check two string are anagram or not")
print("\n 7.Exit")


from itertools import permutations as pm, combinations as cm

def findlength():
    stri = input("Enter a string : ")
    print(f"\nLength of string is : {len(stri)}")

def reverse():
    stri = input("Enter a string : ")
    print(f"\nReverse of string is : {stri[::-1]}")

def palindrome():
    stri = input("Enter a string : ")
    if stri == stri[::-1] :
        print("\nThe entered string is palindrome")
    else :
        print("\nThe entered string is not palindrome")

def symmetrical():
    a = input("Enter a string : ")
    n = len(a)
    flag = 0      
    if n % 2 :
        mid = n//2 +1
        if a[0:mid-1] == a[mid:] :
            print("\nThe entered String is Symmetrical")
        else :
            print("\nThe entered String is not Symmetrical")
    else:
        mid = n//2
        if a[0:mid] == a[mid:] :
            print("\nThe entered String is Symmetrical")
        else :
            print("\nThe entered String is not Symmetrical")

def per_com():
    stri = input("Enter a string : ")
    perm = pm(stri)
    comb = cm(stri,2)
    print("\nPermutation String is :")
    
    for i in list(perm) :
        print(''.join(i))

    print("\nCombination String is :")

    for i in list(comb) :
        print(''.join(i))

def anagram():
    str1 = input("Enter 1st string : ")
    str2 = input("Enter 2nd string : ")
    if(sorted(str1)== sorted(str2)) :
        print("\nThe two strings are anagrams.")
    else:
        print("\nThe two strings are not anagrams.")


    
ch = int(input("Enter your Choice : "))
if ch == 1 :
    findlength()
    
elif ch == 2 :
        reverse()

elif ch == 3 :
        palindrome()

elif ch == 4 :
        symmetrical()

elif ch == 5 :
        per_com()

elif ch == 6 :
        anagram()
    
elif ch == 7 :
        exit()
    
else :
        print("\nWrong Choice")