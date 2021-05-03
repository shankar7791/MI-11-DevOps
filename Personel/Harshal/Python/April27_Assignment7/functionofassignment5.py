def matrix_add() :
    x = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    y = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    z = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

    print("\nMatrix 1 is : ")

    for i in x :
        print(i)

    print("\nMatrix 2 is : ")

    for j in y :
        print(j)

    for i in range(len(x)) :
        for j in range(len(x[0])) :
            z[i][j] = x[i][j] + y[i][j] 

    print("\nAddition of Two Matrices is : ")

    for k in z :
        print(k)

def pall_symm() :
    def palindrome(a) :
        rev = a[::-1]              
        if a == rev:
            print("\nThe entered string is palindrome")
        else:
            print("\nThe entered string is not palindrome")        
        
    def symmetry(a) :
        n = len(a)
        flag = 0      
        if n % 2 :
            mid = n//2 +1
            if a[0:mid-1] == a[mid:] :
                print("\nThe String is Symmetry")
            else :
                print("\nThe String is not Symmetry")
        else:
            mid = n//2
            if a[0:mid] == a[mid:] :
                print("\nThe String is Symmetry")
            else :
                print("\nThe String is not Symmetry")

    string = input("Enter a String : ")
    palindrome(string)
    symmetry(string)
def len_string() :
    str_val = input("Enter a String : ")
    count = 0
    for i in str_val :
        count += 1
    print(f"\nLength of string is : {count}")
def palin() :
    str_in = input("Enter a String : ")
    palin = str_in[::-1]
    if palin == str_in :
        print("\nEntered string is palindrome")
    else :
        print("\nEntered string is not palindrome")

def pascaltri() :
    def fact(num) :
        factorial = 1
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial

    n = 5

    for i in range(n):
        for j in range(n-i+1) :
            print(end = " ")
        for k in range(i+1) :
            print(fact(i) // (fact(k) * fact(i - k)), end=" ")
        print()

while True:
    print("""
    1.Addition of Matrices
    2.Pallindrome and Symmetry
    3.Length of String
    4.Pallindrome
    5.Printing Pascal Triangle
    6.Exit \n""")
    ch = int(input("Enter your Choice : "))
    if ch == 1 :
        print()
        matrix_add()
    
    elif ch == 2 :
        print()
        pall_symm()

    elif ch == 3 :
        print()
        len_string()

    elif ch == 4 :
        print()
        palin()

    elif ch == 5 :
        print()
        pascaltri()

    elif ch == 6 :
        exit()
 