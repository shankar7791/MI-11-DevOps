def Remove_empty(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 

tuples = [(), ('pooja','10','100'), (), ('1','2','3'),('john', 'harry'), (), ('',''),()]
print(Remove_empty(tuples)) 