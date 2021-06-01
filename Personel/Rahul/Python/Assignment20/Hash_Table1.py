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

insert (HashTable, 10)
insert (HashTable, 25)
insert (HashTable, 12)
insert (HashTable, 9 )
insert (HashTable, 8)
insert (HashTable, 17)

display(HashTable)