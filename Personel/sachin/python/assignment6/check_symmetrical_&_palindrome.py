def check_palindrome(value) :
    check_palindrome = value[::-1]
    if check_palindrome == value :
        print("string is palindrome")
    else :
        print("string is not palindrome")

def check_symmetrical(value) :
    
    value_length = len(value)

    mid = value_length // 2

    print(value[mid:value_length])

    if value[0:mid] == value [mid:value_length] :
    
        print ("string is symmetrical ")
    
    else :
    
        print ("string is not symmetrical ")

user_choice = input("Enter a string : ")
check_palindrome(user_choice)
check_symmetrical(user_choice)