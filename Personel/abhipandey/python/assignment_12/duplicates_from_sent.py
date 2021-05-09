from collections import Counter

def remove_duplicates(input):

	input = input.split(" ")

	for i in range(0, len(input)):
		input[i] = "".join(input[i])

	Uniqe = Counter(input)

	s = " ".join(Uniqe.keys())
	print (s)

if __name__ == "__main__":
	str = input("Enter Sentence :")
	remove_duplicates(str)