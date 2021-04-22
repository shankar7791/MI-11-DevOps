a = input("enter the string : ")
def flen(a):
    counter = 0
    for i in a:
        counter += 1
    return counter
print("length of the string is: " ,flen(a))