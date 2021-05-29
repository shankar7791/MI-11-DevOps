class Node :
    def __init__(self, id, name, batch):
        self.id = id
        self.name = name
        self.batch = batch
        self.next = None
        self.prev = None


class Doubly_LinkedList:
    def __init__(self):  
        self.head = None

    def insert(self, newNode) :
        if(self.head is not None) :
            current = self.head
            while(current.next is not None) :
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode

    def printList(self) :
        temp = self.head
        print("[NULL]<--->",end="")
        while(temp) :
            print(f"[{temp.id},{temp.name},{temp.batch}]<--->",end="")
            temp = temp.next
        print("[NULL]")

    def search(self, id) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                print(f"\nStudent ID Found")
                print(f"\nStudent ID : {temp.id} \nStudent Name : {temp.name} \nStudent Batch : {temp.batch}")
                break
            temp = temp.next
        else :
            print("\nStudent ID {id} not Found")

    def delete(self, id) :
        temp = self.head
        if temp is not None :
            if temp.id == id:
                self.head = temp.next
                temp.next.prev = None
                temp = None
                return
        while(temp is not None) :
            if temp.id == id :
                break
            temp = temp.next
        if temp == None :
            return -1
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
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
            print("\nStudent ID not found")

    
llist = Doubly_LinkedList()

while(True):
    print('''
    1. Insert
    2. Display
    3. Search
    4. Delete
    5. Update
    6. Exit''')

    print()
    ch = int(input("Enter Your Choice : "))
    
    if ch == 1 :
        print()
        id = int(input("Enter the Student ID : "))
        name = input("Enter the Student Name : ")
        batch = input("Enter the Student Batch : ")
        newNode = Node(id, name, batch)
        llist.insert(newNode)

    elif ch == 2 :
        llist.printList()

    elif ch == 3 :
        id = int(input("Enter the Student ID : "))
        llist.search(id)

        
    elif ch == 4 :
        id = int(input("\nEnter Student ID :"))
        llist.delete(id)
        '''val = int(input("Enter the Student to be deleted : "))
        op = llist.delete(val)
        if op == -1 :
            print(f"\n Student ID {val} does not exist in the Linked List")
        else :
            print(f"\n Deleted Student ID {val} from the linked list")
'''
    elif ch == 5 :
        id = int(input("Enter the Student ID : "))
        name = input("Enter the Student Name : ")
        batch = input("Enter the Student Batch : ")
        llist.update(id, name, batch)
        
    elif ch == 6 :
        exit()

    else :
        print("\nWrong Choice!!!")