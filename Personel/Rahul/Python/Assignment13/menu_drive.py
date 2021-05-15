print("\n Choose the Given Option : ")
print("1.insert")
print("2.Display")
print("3.Delete")
print("4.Update")
print("5.Reverse")
print("6.Exit")


def insert():
    list = ['1','2','3']  
    for l in list:  
        print(l)  
    list.insert(3,4)  
    print("After insert:")  
    for l in list:
        print(l)  

def display():
    a = [1, 2, 3, 4, 5]
    for x in range(len(a)):
        print (a[x])

def delete():
    list1 = [ 10, 20, 23, 40, 45, 50] 
    list1.remove(45) 
    print("after Delete -",list1) 

def update():
    list1 = [1, 2, 3, 4] 
    list2 = [1, 4, 2, 3, 5] 
    alphabet_set = {'a', 'b', 'c'}
  
    set1 = set(list2) 
    set2 = set(list1)
    set1.update(set2) 
   
    print(set1) 
  
    set1.update(alphabet_set)
    print(set1)

def reverse():
    stri = input("Enter a string : ")
    print(f"\nReverse of string is : {stri[::-1]}")



ch = int(input("Enter your Choice : "))
if ch == 1 :
    insert()

elif ch == 2 :
    display()

elif ch == 3 :
    delete()

elif ch == 4 :
    update()
    
elif ch == 5 :
    reverse()

elif ch == 6 :
     exit()
    
else :
        print("\nWrong Choice")

