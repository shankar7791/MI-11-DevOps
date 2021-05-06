
def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
values = input("enter some comma seprated entry : ")
list = values.split(",")
tup = tuple(list)
print(Reverse(tup))

