class Node :
    def __init__(self, id, name, batch):
        self.id = id
        self.name = name
        self.batch = batch
        self.next = None

class Linked_List :
    def __init__(self) :
        self.head = None 

    def insert(self, newNode) :
        if self.head == None :
            self.head = newNode 
        else :
            temp = self.head
            while (temp) :
                temp.next = newNode
                newNode.next = None
                temp = temp.next 

    def printList(self) :
        temp = self.head
        print("\n")
        while(temp):
            print(f"[{temp.id} {temp.name} {temp.batch}]---->",end="")
            temp = temp.next
        print("Null\n")

    def search(self, id) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                print(f"\nStudent Id {id} Found!!!")
                print(f"Student Id :{temp.id}\nStudent Name : {temp.name}\nStudent Batch : {temp.batch}", end="")
                break
            else :
                temp = temp.next
        else :
            print(f"\nStudent Id {id} NOT Found!!!")

    def delete(self,value) :
        temp = self.head
        if temp is not None :
            if temp.id == value:
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.id == value :
                break
            prev = temp
            temp = temp.next
        if temp == None :
            return -1
        prev.next = temp.next
        temp = None

    def update(self, id, name, batch) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                temp.name = name
                temp.batch = batch
                break
            temp = temp.next
        else :
            print("\nNot Update")



llist = Linked_List()

while(True):
    print('''
    1. Insert
    2. Display
    3. Search
    4. Delete
    5. Update
    6. Exit''')

    ch = int(input("\nEnter your choice :"))

    if ch == 1 :
        id = int(input("\nEnter Student ID :"))
        name = input("\nEnter Student Name :")
        batch = input("\nEnter Student Batch :")
        newNode = Node(id, name, batch)
        llist.insert(newNode)

    elif ch == 2 :
        llist.printList()

    elif ch == 3 :
        id = int(input("\nEnter Student ID :"))
        llist.search(id)

    elif ch == 4 :
        id = int(input("\nEnter Student ID :"))
        llist.delete(id)
     
    elif ch == 5 :
        id = int(input("\nEnter Student ID : "))
        name = input("\nEnter Student Name : ")
        batch = input("\nEnter Student Batch : ")
        llist.update(id, name, batch)
    
    elif ch == 6 :
        exit()


