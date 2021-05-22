# Convert tuple in to dictionary
def Convert(tup, di):
    di = dict(tup)
    return di
      
tups = [("Akshay", 20), ("Shital", 12), ("Ram", 28), ("Tanmay", 20), ("Meena", 25), ("Raj", 30)]
dictionary = {}
print (Convert(tups, dictionary))
