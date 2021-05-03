def palindrome(a):
    rev = a[::-1]              
    if a == rev:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")        
      
def symmetry(a):
    n = len(a)
    flag = 0      
    if n % 2 :
        mid = n//2 +1
        if a[0:mid-1] == a[mid:] :
            print("The String is Symmetry")
        else :
            print("The String is not Symmetry")
    else:
        mid = n//2
        if a[0:mid] == a[mid:] :
            print("The String is Symmetry")
        else :
            print("The String is not Symmetry")

string = input("Enter a String")
palindrome(string)
symmetry(string)