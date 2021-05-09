def Remove(tuples) :
    tuples = [t for t in tuples if t]      
    return tuples

tup = [1,2,'Harshal',(),("Harry","Narvekar"),()]
print(Remove(tup))