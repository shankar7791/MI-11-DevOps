class Node:
    def __init__(self, id, name, batch):
       self.id = id
       self.name = name 
       self.batch = batch 
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, newNode):
        if self.last_node is None:
            self.head = newNode 
            self.last_node = self.head
        else:
            self.last_node.next = newNode
            self.last_node = self.last_node.next
 
    def display(self):
        if self.head == None :
            print("nothing to display plz add some data in node first ")
        else :
            current = self.head
            while current is not None:
                print(f"[{current.id} {current.name} {current.batch}--->]" , end ="")
                current = current.next
            print(" Null")

    def search(self, id):
        if self.head == None :
            print("nothing to search plz add some data in node first ")
        else:
            current = self.head 
            while current is not None:
                if current.id == id:
                    print(f"Id has been found ", end = " " )
                    print(f"[{ current.id} {current.name} {current.batch}]", end = "")
                    current = current.next
                    break
                current = current.next 
            else :
                 print("Id not found")
    
    def delete (self, id) : 
        pass 
                
    def update(self, id):
        if self.head == None :
            print("nothing to update plz add some data in node first ")
        else : 
            current = self.head 
            flag = 1
            print ("PPPPPPPPPPPPPPP")
            while current is not None :
                print (f"jkkdkkdkdkdk :::::::::::::;; {current.id}  {id}")
                if current.id == id :
                    print("update id has been found ")
                    a_llist.display()
                    print('''select the option you want to update
                    1. update Name 
                    2. update Batch
                    ''') 
                    temp_var= input()
                    if temp_var == 1 : 
                        current.name = input("enter the updtaed name : ")
                    elif temp_var == 2 : 
                        current.batch = input("enter the updated batch name : ")
                    else : 
                        print("you have enter the wrong input !!!!!!!")
                        flag = 0 

                    ''' if flag == 0 :
                    pass ''' 
                else :
                    current = current.next 
            print(f"\n updated linklist : {a_llist.display() }" , end ="")

                
                    
a_llist = LinkedList()

while(True):

    print('''*************************************************************************************************************************************
    choose the following option to perform task 
    1.append the linklist
    2.display 
    3.search 
    4.delete 
    5.update 
    6.exit  
*************************************************************************************************************************************
    ''')
    user_choice=int(input())
       
    if user_choice == 1 :
        n = int(input('\n How many elements would you like to add? '))
        for i in range(n):
            id = int(input('\nEnter ID of a student : '))
            name = input('\n Enter Name  of a student : ')
            batch = input('\n Enter BATCH of a student : ')
            newNode = Node(id, name, batch)
            a_llist.append(newNode)

    elif user_choice == 2 : 
        a_llist.display()

    elif user_choice == 3 :
        search_input = int(input("\n enter the ID that need to  be searched : "))
        a_llist.search(search_input)

    elif user_choice == 4 :
        delete_input = input("\n enter the ID that need to be get deleted : ")
        a_llist.delete(delete_input)

    elif user_choice == 5 :
        update_input = input("\n enter the ID that need to be get update : ")
        a_llist.update(update_input)

    if  user_choice == 6 :
        print("exiting the program")
        break 
    
    else :
        print ("\n ********************************************************** CTRl+F5 ***************************************************")