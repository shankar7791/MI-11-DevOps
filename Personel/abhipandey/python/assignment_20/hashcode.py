def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  
def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
  
insert(HashTable, 10 , "10")
insert(HashTable, 20, "30")
insert(HashTable, 30 , '60')
insert(HashTable, 15,"90")
insert(HashTable, 21,"66")
insert(HashTable, 21 , "33")
  
display_hash (HashTable)