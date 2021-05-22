#Remove empty tuple from list.
def Remove_empty(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [("patil","akkii",),(1,3,45,), (),('shamli','simu'), (),()]
print(Remove_empty(tuples)) 
