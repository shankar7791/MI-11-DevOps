def findLen(str):
    count = 0
    for i in str :
        count += 1
    return count

str = input("Enter the string :")
print("Length of a String :",findLen(str))