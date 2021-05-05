def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 
# Driver Code
tuples = [(), ('Rahul','Ramesh','Gupta'), (), ('Jerry', 'Rajj'), 
          ('Java', 'Python', '00'), ('',''),('Rohan','253'),()]
print(Remove(tuples)) 