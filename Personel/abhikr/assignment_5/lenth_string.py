#prog 5.4.

def findLen(str):
    count = 0 
    space =0   
    for i in range(0,len(str)):
        if str[i] ==" ":
            space +=1
        count += 1
    x = count-space
    return x
    
  
my_str  = input("Input a string: ")
  

print(findLen(my_str))