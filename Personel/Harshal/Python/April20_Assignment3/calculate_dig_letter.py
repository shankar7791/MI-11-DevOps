str_val = input("Enter a String : ")
digit = 0
letter = 0
for i in str_val :
    if i.isdigit() :
        digit += 1
    else :
        letter += 1
print(f"Number of digits in string is {digit} and Number of letter in string is {letter}")