import array as arry

def LS(arr, val) :
    for i in range(len(arr)) :
        if val == arr[i] :
            return i
    
    else :
        return -1

arr = arry.array("i", [33, 47, 99, 2, 10, 444, 88, 77, 41])
val = int(input("enter the search value: "))
ind = LS(arr, val)

if ind == -1 :
    print(f"Given Value {val} is not present")
else:
    print(f"Given Value {val} found at index  {ind}")