user_choice = input("Enter a string : ")
palindrome = user_choice[::-1]
if palindrome == user_choice :
    print("string is palindrome")
else :
    print("string is not palindrome")