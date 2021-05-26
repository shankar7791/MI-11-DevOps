import array as arry

def linearSearch(arr, val) :
    for i in range(len(arr)) :
        if val == arr[i] :
            return i
    
    else :
        return -1

arr = arry.array("i", [14, 21, 27, 41, 43, 45, 46, 57, 70])
val = 45
ind = linearSearch(arr, val)

if ind == -1 :
    print(f"Given Value {val} not found in array")
else:
    print(f"Given Value {val} found at index position {ind}")