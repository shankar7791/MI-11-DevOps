from itertools import groupby
def rmc(input):
	
	result = []
	for (key,group) in groupby(input):
		result.append(key)

	print (''.join(result))
	
input = input("Enter Word Or Sentence: ")
rmc(input)
