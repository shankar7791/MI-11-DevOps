def palin(str_in) :
    palin = str_in[::-1]
    if palin == str_in :
        print("Entered string is palindrome")
    else :
        print("Entered string is not palindrome")
val_str = input("Enter a String : ")
palin(val_str)