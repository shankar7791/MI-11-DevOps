def insertion_sort(list1):  
  
        for i in range(1, len(list1)):  
  
            value = list1[i]  

            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        return list1  
  
list1 =[55, 40, 90, 13, 5, 22, 44]  
print("The unsorted list is:", list1)  
print("The sorted list1 is:", insertion_sort(list1))  