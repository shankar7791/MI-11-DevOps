def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
       
tups = [("rahul", 50), ("rohit", 12), ("raj", 14), 
     ("sanket", 20), ("sonu", 25), ("sumit", 30)]
dictionary = {}
print (Convert(tups, dictionary))