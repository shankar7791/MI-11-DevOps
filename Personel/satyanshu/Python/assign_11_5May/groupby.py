from itertools import groupby
def removeAllConsecutive(inp):
	result = []
	for (key,group) in groupby(inp):
		result.append(key)

	print (''.join(result))
	
inp = input("enter string : ")
removeAllConsecutive(inp)

