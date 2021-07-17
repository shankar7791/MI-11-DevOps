from tabulate import tabulate 
class Node :
    def __init__ (self, id, name, batch, department, address ):
        self.id = id
        self.name = name 
        self.batch = batch
        self.department = department
        self.address = address 
        
    #Doubly LinkedList
class Doubly_LinkedList:
    def __init__ (self, T = [None for _ in range(10)]):
        self.head = None
        self.T = T
        self.m = len(self.T)
        self.size = 0
    #Hash LinkedList Data 
    def hash(self, id):
        return id % self.m
    #Insert Data    
    def insert(self, newnode) :
        k = self.hash(newnode.id)
        if self.T[k] == None:
            self.T[k] = newnode 
            newnode.next = None 
            newnode.prev = None
        else:
            temp = self.T[k]
            while temp.next is not None :
                temp = temp.next
            newnode.prev = temp
            temp.next = newnode
        self.size += 1
    #Display Data
    def display(self) :
        res = [None for _ in range(self.m)]
        for i in range(self.m):
            k = self.T[i] 
            line = '' 
            while k:
                data ="{" + str(k.id) + ", " + str(k.name) + ", " + str(k.batch) + ", " + str(k.department) + ", " + str(k.address) + "}"
                line += data
                k = k.next
                if k:
                    line += ' ==> '
            res[i] = line
        for i in range (len(res)):
            print(res[i])
    #Display Data In Data.txt
    def displaytab(self):
        print("")
        with open("data.txt", "r") as fd:
            f = []
            for line in fd.readlines(): 
                lis = line.split()
                f.append(lis)
            print(tabulate(f, headers = ["ID", "Name", "Batch", "Department", "Address"],))
    
 
    #Searching Data
    def search(self, id) :
        k = self.hash(id)
        node = self.T[k]
        while(node) :
            if node.id == id :
                print(f"\nStudent ID Found ")
                print("\nStudent Details:-")
                print(f"\nStudent ID : {node.id} \nStudent Name : {node.name} \nStudent Batch : {node.batch} \nDepartment : {node.department} \naddress : {node.address}\n")
                break
            node = node.next
        else :
            print("\nStudent ID {id} not Found")
    #Deleting Data
    def delete(self, id) : 
        k = self.hash(id) 
        node = self.T[k] 
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
                self.T[k] = node.next
            else:
                prev.next = prev.next.next 
            return result
     #Updating Data
    def update(self, newnode) :
        k = self.hash(newnode.id)
        node = self.T[k]
        while node:
            if node.id == newnode.id : 
                node.name = newnode.name 
                node.batch = newnode.batch 
                node.department = newnode.department
                node.address = newnode.address
                self.deletef(newnode.id)
                self.write(newnode) 
                break
            node = node.next 
        else :
            print("\nStudent ID not found")


    def write(self,newnode):
        with open("data.txt","a+") as fd:
            fd.writelines( str(newnode.id) +' '+ newnode.name +' '+newnode.batch +' '+newnode.department + ' '+newnode.address +  "\n")

    def readf(self):
        with open("data.txt", "r") as fd:
            f=[]
            for line in fd.readlines(): 
                f= line.split()
                id = f[0] 
                name = f[1] 
                batch = f[2] 
                department = f[3]
                address = f[4]

                newnode = Node(int(id), name, batch, department, address)
                T.insert(newnode)

    def deletef(self, id):
        with open("data.txt","r+") as fd: 
            f = fd.readlines() 
            fd.seek(0)
            for line in f :
                if str(id) not in line: 
                    fd.write(line)
            fd.truncate()


T = Doubly_LinkedList() 
#T.readf()


while(True):
    print('''
        
                 Student Management System
                 
                    1.  Add =
                    2.  Display =
                    3.  Search =
                    4.  Delete =
                    5.  Update =
                    6.  Exit = 
                    ''')

    print()
    ch = int(input("Enter The Choice : "))

    if ch == 1 :
        length = int(input("Enter Number Of Nodes :\n"))
        for counter in range(1, length + 1):
            id = int(input("Enter The Student ID : "))
            name = input("Enter The Student Name : ")
            batch = input("Enter The Student Batch : ")
            department = input("Enter The Department :")
            address = input("Enter The Address :")
            newNode = Node(id, name, batch, department, address)
            T.hash(id)
            T.insert(newNode) 
            T.write(newNode)
        print("\nData has been Added..")

    elif ch == 2 : 
        T.displaytab()

    elif ch == 3 :
        id = int(input("Enter The Student ID : "))
        print(T.search(id))

    
    elif ch == 4 :
        id = int(input("\nEnter Student ID :"))
        T.delete(id)
        T.deletef(id)
        print("\nData Deleted Successfully :")

    elif ch == 5 :
        id = int(input("Enter The Student ID : "))
        name = input("Enter The Student Name : ")
        batch = input("Enter The Student Batch : ")
        department = input("Enter The Department :")
        address = input("Enter The Address :")
        newnode = Node(id, name, batch, department, address)
        T.update(newnode)
        print("\nData update Successfully :")

    elif ch == 6 :
        exit()

    