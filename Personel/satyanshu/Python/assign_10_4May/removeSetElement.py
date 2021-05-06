def Remove(iset):
    while iset:
        iset.pop()
        #return(initial_set)
    print("printing empty set : ",iset)
# Driver Code
iset = input("enter element of set : ")
iset = set(iset)
Remove(iset)

