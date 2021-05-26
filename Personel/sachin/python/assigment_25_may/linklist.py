class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        if self.head == None :
            print("nothing to display plz add some data in node first ")
        else :
            current = self.head
            while current is not None:
                print(current.data, end = ' ')
                current = current.next
            
    def search(self, data):
        if self.head == None :
            print("nothing to search plz add some data in node first ")
        else:
            current = self.head 
            counter = 1
            while current is not None:
                if current.data == data:
                    print(f"Id has been found at {counter} position", end = " " )
                    flag = 1    
                else:
                    flag = 0
                current = current.next
                counter = counter + 1 
            if flag != 1:
                print("Id not found")

a_llist = LinkedList()

while(True):

    print(
    '''
    choose the following option to perform task 
    1.append the linklist
    2.display 
    3.search 
    4.exit  
    '''
    )
    user_choice=int(input())
       
    if user_choice == 1:
        n = int(input('How many elements would you like to add? '))
        for i in range(n):
            data = int(input('Enter data item: '))
            a_llist.append(data)
        print('The linked list: ', end = '')

    elif user_choice == 2:
        a_llist.display()

    elif user_choice == 3:
        search_input = int(input("enter the data that need to get searched"))
        a_llist.search(search_input)
    
    if  user_choice == 4 :
        print("exiting the program")
        break 
    
    else :
        print ("\n running program again ")
