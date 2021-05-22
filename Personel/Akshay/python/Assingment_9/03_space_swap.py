'''Python program to get a single string from two given strings, separated by
a space and swap the first two characters of each string'''


str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
new_str1 = str2[0:2] + str1[2:]
new_str2 = str1[0:2] + str2[2:]
fin_str = new_str1 + " " + new_str2
print (f"String after swapping and concatinating is : \n {fin_str} ")