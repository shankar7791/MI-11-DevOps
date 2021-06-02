def display(hashTable):
    
    for i in range(len(hashTable)) :
        print(i, end = " ")

        for j in hashTable[i] :
            print("-->", end = " ")
            print(j, end = " ")

        print()

HashTable = [[] for _ in range(10)]
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue) :

    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(keyvalue)

insert (HashTable, 11)
insert (HashTable, 21)
insert (HashTable, 20)
insert (HashTable, 5)
insert (HashTable, 3)
insert (HashTable, 47)

display(HashTable)