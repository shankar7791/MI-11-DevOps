# Write a Python function that takes a number as a parameter and check the number is prime or not
def count(str) :
    lower = 0
    upper = 0
    for i in str :
        if i.islower() :
            lower += 1
        elif i.isupper() :
            upper += 1
        else :
            pass
    print (f"Number of Lower case characters in String are : {lower}")
    print (f"Number of Upper case characters in String are : {upper}")
string = input("Enter a String : ")
count(string)