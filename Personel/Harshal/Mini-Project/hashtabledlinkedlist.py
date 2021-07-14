from tabulate import tabulate
class Node :
    def __init__ (self, id, name, batch, city):
        self.id = id
        self.name = name 
        self.batch = batch
        self.city = city 
        self.next = None 
        self.prev = None
    
    def repr (self):
        value = '{%d %s %s %s}' % (self.id, self.name, self.batch, self.city)
        return value

class Doubly_LinkedList:
    def __init__ (self, HashTable = [None for _ in range(10)]):
        self.head = None
        self.HashTable = HashTable
        self.m = len(self.HashTable)
        self.size = 0

    def hash(self, id):
        return id % self.m

    def insert(self, newnode) :
        k = self.hash(newnode.id)
        if self.HashTable[k] == None:
            self.HashTable[k] = newnode 
            newnode.next = None 
            newnode.prev = None
        else:
            temp = self.HashTable[k]
            while temp.next is not None :
                temp = temp.next
            newnode.prev = temp
            temp.next = newnode
        self.size += 1
        # HashTable.display()

    def display(self) :
        res = [None for _ in range(self.m)]
        for i in range(self.m):
            k = self.HashTable[i] 
            line = '' 
            while k:
                data ="{" + str(k.id) + ", " + str(k.name) + ", " + str(k.batch) + ", " + str(k.city) + "}"
                line += data
                k = k.next
                if k:
                    line += ' <=> '
            res[i] = line
        for i in range (len(res)):
            print(res[i])

    def displaytab(self):
        print("")
        with open("scam1992.txt", "r") as fd:
            f = []
            for line in fd.readlines(): 
                lis = line.split()
                f.append(lis)
            print(tabulate(f, headers = ["ID", "Name", "Batch", "City"], tablefmt='psql'))
 
    def search(self, id) : 
        k = self.hash(id) 
        node = self.HashTable[k]
        while node is not None and node.id != id: 
            node = node.next
        if node is None: 
            return None
        else:
            return node

    def delete(self, id) : 
        k = self.hash(id) 
        node = self.HashTable[k] 
        prev = None

        while node is not None and node.id != id: 
            prev = node
            node = node.next

        if node is None: 
            return None
        else:
            self.size -= 1 
            result = node
            if prev is None: 
                self.HashTable[k] = node.next
            else:
                prev.next = prev.next.next 
            return result

    def update(self, newnode) :
        k = self.hash(newnode.id)
        node = self.HashTable[k]
        while node:
            if node.id == newnode.id : 
                node.name = newnode.name 
                node.batch = newnode.batch
                node.city = newnode.city
                self.deletef(newnode.id)
                self.write(newnode) 
                break
            node = node.next 
        else :
            print("\nStudent ID not found")       

        print("Updated node :")


    def write(self,newnode):
        with open("scam1992.txt","a+") as fd:
            fd.writelines( str(newnode.id) +' '+ newnode.name +' '+newnode.batch + ' '+newnode.city+ "\n")

    def readf(self):
        with open("scam1992.txt", "r") as fd:
            f=[]
            for line in fd.readlines(): 
                f= line.split()
                id = f[0] 
                name = f[1] 
                batch = f[2] 
                city = f[3]
                newnode = Node(int(id), name, batch, city)
                HashTable.insert(newnode)

    def deletef(self, id):
        with open("scam1992.txt","r+") as fd: 
            f = fd.readlines() 
            fd.seek(0)
            for line in f :
                if str(id) not in line: 
                    fd.write(line)
            fd.truncate()

HashTable = Doubly_LinkedList() 
HashTable.readf()


while(True):
    print('''
        *******************************************
        =========Student Management System=========
        *******************************************
        1.	Add
        2.	Display
        3.	Search
        4.	Delete
        5.	Update
        6.	Exit
        -------------------------------------------''')

    print()
    ch = int(input("Enter Your Choice : "))

    if ch == 1 :
        length = int(input("Enter the number of nodes you want for your Linked List:\n"))
        for counter in range(1, length + 1):
            id = int(input("Enter the Student Roll No. : "))
            name = input("Enter the Student Name : ")
            batch = input("Enter the Student Batch : ")
            city = input("Enter City :")
            newNode = Node(id, name, batch, city)
            HashTable.hash(id)
            HashTable.insert(newNode) 
            HashTable.write(newNode)
        print("Data has been Added..")

    elif ch == 2 : 
        HashTable.displaytab()

    elif ch == 3 :
        id = int(input("Enter the Student ID : "))
        data = HashTable.search(id)
        print(f"ID :- {data.id}")
        print(f"Name :- {data.name}")
        print(f"Batch :- {data.batch}")
        print(f"City :- {data.city}")

    elif ch == 4 :
        id = int(input("\nEnter Student ID :"))
        HashTable.delete(id)
        HashTable.deletef(id)
        print("Data Deleted Successfully :")

    elif ch == 5 :
        id = int(input("Enter the Student ID : "))
        name = input("Enter the Student Name : ")
        batch = input("Enter the Student Batch : ")
        city = input("Enter City : ")
        newnode = Node(id, name, batch, city)
        HashTable.update(newnode)
        print("Data update Successfully :")

    elif ch == 6 :
        exit()

    else :
        print("\nWrong Choice!!!")

