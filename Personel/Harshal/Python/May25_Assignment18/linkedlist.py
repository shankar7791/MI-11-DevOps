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

if __name__=='__main__':
    ll = LinkedList()
    while True :
        print("""
        1.Add Data to Linked list
        2.Print Linked List
        3.Exit""")
        ch = int(input("Enter Your Choice : "))
        if ch == 1 :
            val = int(input("Enter the Value to insert : "))
            ll.insert(val)

        elif ch == 2 :
            ll.printll()
        
        elif ch == 3 :
            exit()
        
        else :
            print("Wrong Input")

