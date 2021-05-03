
from itertools import permutations as pm, combinations as cm

def leng():
    str1 = input("Enter a string : ")
    print(f"\nLength of the given string is {len(str1)}")

def rev():
    str1 = input("Enter a string : ")
    print(f"Reverse of the given string is {str1[::-1]}")

def pal():
    str1 = input("Enter a string : ")
    if str1 == str1[::-1] :
        print(" string is palindrome")
    else :
        print(" string is not palindrome")

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
            print(" String is Symmetry")
        else :
            print("Entered String is not Symmetry")

def percom():
    str1 = input("Enter a string : ")
    perm = pm(str1)
    comb = cm(str1,2)
    print("Permutation of String is :")
    
    for i in list(perm) :
        print(''.join(i))

    print("Combination of String is :")

    for i in list(comb) :
        print(''.join(i))

def anagram():
    str1 = input("Enter first string : ")
    str2 = input("Enter second string : ")
    if(sorted(str1)== sorted(str2)) :
        print("The two strings are anagrams.")
    else:
        print("The two strings are not anagrams.")

while True:
    print("""
    1.Length 
    2.Reverse 
    3.Palindrome 
    4.Symmetrical 
    5.Permutation and Combination
    6. anagram or Not
    7.Exit """)
    
    print()
    
    ch = int(input("Enter your Choice : "))
    
    if ch == 1 :
        length()
    
    elif ch == 2 :
        rev()

    elif ch == 3 :
        pal()

    elif ch == 4 :
        sym()

    elif ch == 5 :
        percom()

    elif ch == 6 :
        anagram()
    
    elif ch == 7 :
        exit()
    
    else :
        print("\nWrong Choice")