import array as arry
def bs(arr, lh, rh, val) :
    while lh <= rh :
        mid = lh + (rh - lh) // 2
        if arr[mid] == val :
            return mid
        elif arr[mid] < val :
            lh = mid + 1
        else :
            rh = mid - 1

    return -1

arr = arry.array("i", [33, 47, 99, 2, 10, 444, 88, 77, 41])
val = int(input("enter the search value: "))

ind = bs(arr, 1, len(arr) - 1, val)

if ind == -1 :
    print(f"Given Value {val} is not present")
else:
    print(f"Given Value {val} found at index {ind}")