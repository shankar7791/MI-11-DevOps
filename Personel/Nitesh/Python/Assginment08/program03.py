def sum_arr(arr,size):
   if (size == 0):
     return 0
   else:
     return arr[size-1] + sum_arr(arr,size-1)
n=int(input("Enter the total number list:"))
a=[]
for i in range(0,n):
    element=int(input("Enter number :"))
    a.append(element)
print("The list is:")
print(a)
print("Sum of a list of numbers:")
b=sum_arr(a,n)
print(b)