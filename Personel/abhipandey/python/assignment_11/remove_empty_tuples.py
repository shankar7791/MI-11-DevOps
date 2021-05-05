def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 
# Driver Code
tuples = [(), ('tony','20','10'), (), ('steve', 'natasha'), 
          ('bruce', 'thor', '45'), ('',''),()]
print(Remove(tuples)) 