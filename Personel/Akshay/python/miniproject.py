from tabulate import tabulate 

class Node :
    def __init__ (self, id, name, batch, department, address ):
        self.id = id
        self.name = name 
        self.batch = batch
        self.department = department
        self.address = address 
        self.next = None 
        self.prev = None
    
    def repr (self):
        value = '{%d %s %s %s %s}' % (self.id, self.name, self.batch, self.department, self.address )
        return value

class Doubly_LinkedList:
    def __init__ (self, T = [None for _ in range(10)]):
        self.head = None
        self.T = T
        self.m = len(self.T)
        self.size = 0

    def hash(self, id):
        return id % self.m

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

    def displaytab(self):
        print("")
        with open("stud.txt", "r") as fd:
            f = []
            for line in fd.readlines(): 
                lis = line.split()
                f.append(lis)
            print(tabulate(f, headers = ["ID", "Name", "Batch", "Department", "Address"], tablefmt='psql'))
    
 

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
        with open("stud.txt","a+") as fd:
            fd.writelines( str(newnode.id) +' '+ newnode.name +' '+newnode.batch +' '+newnode.department + ' '+newnode.address +  "\n")

    def readf(self):
        with open("stud.txt", "r") as fd:
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
        with open("stud.txt","r+") as fd: 
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
        *******************************************
        =========Student Management System=========
        *******************************************
                    1. Add -
                    2. Display -
                    3. Search -
                    4. Delete -
                    5. Update -
                    6. Exit - 
        
        *******************************************
        *******************************************''')

    print()
    ch = int(input("Enter Your Choice : "))

    if ch == 1 :
        length = int(input("Enter the No. of Nodes.. :\n"))
        for counter in range(1, length + 1):
            id = int(input("Enter the Student ID. : "))
            name = input("Enter the Student Name : ")
            batch = input("Enter the Student Batch : ")
            department = input("Enter Department :")
            address = input("Enter Address :")
            newNode = Node(id, name, batch, department, address)
            T.hash(id)
            T.insert(newNode) 
            T.write(newNode)
        print("\nData has been Added..")

    elif ch == 2 : 
        T.displaytab()

    elif ch == 3 :
        id = int(input("Enter the Student ID : "))
        print(T.search(id))

    
    elif ch == 4 :
        id = int(input("\nEnter Student ID :"))
        T.delete(id)
        T.deletef(id)
        print("\nData Deleted Successfully :")

    elif ch == 5 :
        id = int(input("Enter the Student ID : "))
        name = input("Enter the Student Name : ")
        batch = input("Enter the Student Batch : ")
        department = input("Enter Department :")
        address = input("Enter Address :")
        newnode = Node(id, name, batch, department, address)
        T.update(newnode)
        print("\nData update Successfully :")

    elif ch == 6 :
        exit()

    else :
        print("\nWrong Choice!!!")