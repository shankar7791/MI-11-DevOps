import string

alphabet = set(string.ascii_lowercase)

def ispangram(string):
	return set(string.lower()) >= alphabet
	
string = input("Enter the Sentence :")
if(ispangram(string) == True):
	print("The Sentence is Panagram")
else:
	print("The Sentence is not Panagram")

