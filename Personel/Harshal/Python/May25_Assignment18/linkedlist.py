class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self.head is not None):
            current = self.head
            while(current.next is not None):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def printll(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def delete(self, val) :
        temp = self.head
        if temp is not None :
            if temp.data == val:
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == val :
                break
            prev = temp
            temp = temp.next
        if temp == None :
            return -1
        prev.next = temp.next
        temp = None

if __name__=='__main__':
    ll = LinkedList()
    while True :
        print("""
        1.Add Data to Linked list
        2.Print Linked List
        3.Delete Data From Linket List
        4.Exit""")
        ch = int(input("Enter Your Choice : "))
        if ch == 1 :
            val = int(input("Enter the Value to insert : "))
            ll.insert(val)

        elif ch == 2 :
            ll.printll()
        
        elif ch == 3 :
            val = int(input("Enter the data to be deleted : "))
            op = ll.delete(val)
            if op == -1 :
                print(f"Value {val} does not exist in the Linked List")
            else :
                print(f"Deleted Value {val} from the linked list")

        elif ch == 4 :
            exit()
            
        else :
            print("Wrong Input")

