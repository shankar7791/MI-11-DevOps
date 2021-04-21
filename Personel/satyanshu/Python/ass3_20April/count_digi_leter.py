str = input("Enter a String : ")
digit = 0
letter = 0
for i in str :
    if i.isdigit() :
        digit += 1
    else :
        letter += 1
print(f"Number of digits is {digit} and Number of letter is {letter}")
