def ins(val) :
    lis.extend(val)

def disp() :
    print("List is \n ", lis)

def dele(val) :
    lis.remove(val)

def up(val1,val2) :
    i = lis.index(val1)
    lis[i] = val2

def rev() :
    print("Reverse of the list is : \n", lis[::-1])

lis = []

while True :
    print("""
    List Operations :
    1.Insert
    2.Display
    3.Delete
    4.Update
    5.Reverse
    6.Exit""")
    
    cho = int(input("Enter your choice : "))
    
    if cho == 1 :
        lis1 = [int(item) for item in input("Enter the numbers to add to the list : ").split()]
        ins(lis1)
    
    elif cho == 2 :
        disp()
    
    elif cho == 3 :
        val = int(input("Enter a number to remove from the list : "))
        dele(val)
    
    elif cho == 4 :
        val1 = int(input("Enter a number to update from the list : "))
        val2 = int(input("Enter the number to update : "))
        up(val1,val2)
    
    elif cho == 5 :
        rev()
    
    elif cho == 6 :
        exit(0)
    
    else :
        print("Wrong Choice Selected")

