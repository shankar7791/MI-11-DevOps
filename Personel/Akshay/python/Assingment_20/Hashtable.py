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

def insert(Hashtable, keyvalue, value) :

    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert (HashTable, 11, 10)
insert (HashTable, 3, 33)
insert (HashTable, 4, 15)
insert (HashTable, 9,  39)
insert (HashTable, 20, 31)
insert (HashTable, 11, 41)

display(HashTable)