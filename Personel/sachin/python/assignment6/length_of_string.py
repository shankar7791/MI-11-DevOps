def length_of_string(argument): 
    count = 0
    for i in user_choice:
        count += 1
    return count

user_choice= input("Enter a String : ")
x = length_of_string(user_choice)
print(f"Length of a string is : {x}")