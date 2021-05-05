# function to remove all consecutive duplicates
# from the string in Python

from itertools import groupby
def rmc(input):
	
	result = []
	for (key,group) in groupby(input):
		result.append(key)

	print (''.join(result))
	
# Driver program

input = input("enter the word or sentence: ")
rmc(input)
