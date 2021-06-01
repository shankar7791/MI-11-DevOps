def linear_Search(list1, n, key):  
      
        for i in range(0, n):  
            if (list1[i] == key):  
                return i  
        return -1  

list1 = [5, 9, 77, 56, 99, 18, 78]  
key = 18
      
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
     print("Element not found")  
else:  
     print("Element found at index: ", res)  
