def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 
# Driver Code
tuples = [(), ('Nitesh','Tribhuvan','Jaiswar'), (), ('nitesh', 'vicky'), 
          ('Java', 'Python', '00'), ('',''),('vinayak','253'),()]
print(Remove(tuples)) 