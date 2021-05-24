import array as arry
def binarySearch(arr, lh, rh, val) :
    while lh <= rh :
        mid = lh + (rh - lh) // 2
        if arr[mid] == val :
            return mid
        elif arr[mid] < val :
            lh = mid + 1
        else :
            rh = mid - 1

    return -1

arr = arry.array("i", [14, 21, 27, 41, 43, 45, 46, 57, 70])
val = 57

ind = binarySearch(arr, 0, len(arr) - 1, val)

if ind == -1 :
    print(f"Given Value {val} not found in array")
else:
    print(f"Given Value {val} found at index position {ind}")