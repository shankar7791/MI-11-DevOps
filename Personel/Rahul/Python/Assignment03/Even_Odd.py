num= (12, 34, 83, 39, 61, 64, 90, 55, 70, 23, 60, 54, 22) 
print(num)
odd = 0
even = 0
for x in num:
        if not x % 2:
    	     even +=1
        else:
    	     odd +=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
