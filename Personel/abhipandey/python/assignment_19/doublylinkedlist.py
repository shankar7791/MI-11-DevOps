class Node :
    def __init__(self, id, name, batch) : 
        self.id = id
        self.name = name
        self.batch = batch
        self.next = None
        self.prev = None

class Doublellist:
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

    def printdll(self) :
        temp = self.head
        print()
        print("[NULL]<---")
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
            print("\nStudent ID not Found")

    def update(self, id, new_name, new_batch) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                temp.name = new_name
                temp.batch = new_batch
                break
            temp = temp.next
        else :
            print("\nStudent ID not found.")

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
    
dll = Doublellist()

while True :
    print("""
    1.Add Data
    2.Print
    3.Delete 
    4.Search
    5.Update 
    6.Exit""")
    print()
    choice = int(input("Enter Your Choice : "))
    if choice == 1 :
        print()
        id = int(input("Enter the Student ID : "))
        name = input("Enter the Student Name : ")
        batch = input("Enter the Student Batch : ")
        newNode = Node(id, name, batch)
        dll.insert(newNode)

    elif choice == 2 :
        print()
        dll.printdll()
        
    elif choice == 3 :
        print()
        val = int(input("Enter the Student to be deleted : "))
        op = dll.delete(val)
        if op == -1 :
            print(f"\n Student ID {val} does not exist .")
        else :
            print(f"\n Deleted Student ID {val} .")

    elif choice == 4 :
        print()
        id = int(input("Enter the Student ID : "))
        dll.search(id)

    elif choice == 5 :
        print()
        id = int(input("Enter the Student ID : "))
        name = input("Enter the Student Name : ")
        batch = input("Enter the Student Batch : ")
        dll.update(id, name, batch)
        
    elif choice == 6 :
        exit()

    else :
        print("\nWrong Input")