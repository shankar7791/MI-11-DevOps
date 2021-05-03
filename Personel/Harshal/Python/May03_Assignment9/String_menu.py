from itertools import permutations as pm, combinations as cm

def length():
    stri = input("Enter a string : ")
    print(f"\nLength of the given string is {len(stri)}")

def rev():
    stri = input("Enter a string : ")
    print(f"\nReverse of the given string is {stri[::-1]}")

def palin():
    stri = input("Enter a string : ")
    if stri == stri[::-1] :
        print("\nEntered string is palindrome")
    else :
        print("\nEntered string is not palindrome")

def sym():
    a = input("Enter a string : ")
    n = len(a)
    flag = 0      
    if n % 2 :
        mid = n//2 +1
        if a[0:mid-1] == a[mid:] :
            print("\nEntered String is Symmetry")
        else :
            print("\nEntered String is not Symmetry")
    else:
        mid = n//2
        if a[0:mid] == a[mid:] :
            print("\nEntered String is Symmetry")
        else :
            print("\nEntered String is not Symmetry")

def per_com():
    stri = input("Enter a string : ")
    perm = pm(stri)
    comb = cm(stri,2)
    print("\nPermutation of String is :")
    
    for i in list(perm) :
        print(''.join(i))

    print("\nCombination of String is :")

    for i in list(comb) :
        print(''.join(i))

def anagram():
    str1 = input("Enter first string : ")
    str2 = input("Enter second string : ")
    if(sorted(str1)== sorted(str2)) :
        print("\nThe two strings are anagrams.")
    else:
        print("\nThe two strings are not anagrams.")

while True:
    print("""
    1.Length of String
    2.Reverse of String
    3.Check Palindrome or Not
    4.Check Symmetrical or Not
    5.Check Permutation and Combination
    6.Check two strings are anagram or Not
    7.Exit """)
    
    print()
    
    ch = int(input("Enter your Choice : "))
    
    if ch == 1 :
        length()
    
    elif ch == 2 :
        rev()

    elif ch == 3 :
        palin()

    elif ch == 4 :
        sym()

    elif ch == 5 :
        per_com()

    elif ch == 6 :
        anagram()
    
    elif ch == 7 :
        exit()
    
    else :
        print("\nWrong Choice")