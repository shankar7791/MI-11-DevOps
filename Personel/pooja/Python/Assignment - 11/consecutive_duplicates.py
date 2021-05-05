from itertools import groupby
def remove_all_consecutive(str1):
    result_str = []
    for (key,group) in groupby(str1):
        result_str.append(key)

    return ''.join(result_str)

str1 = input("Enter string:")
print("Original string:" + str1)
print("After removing consecutive duplicates:" )
print(remove_all_consecutive(str1))