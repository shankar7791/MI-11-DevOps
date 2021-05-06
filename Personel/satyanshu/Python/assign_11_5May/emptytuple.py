
def Remove(tuple1):
    tuples = [t for t in tuple1 if t]
    return tuples
values = input("Enter a list with empty tuples in it. ")
print('List : ',values)
print ("after removing empty tuple : ")
print (Remove(values))
