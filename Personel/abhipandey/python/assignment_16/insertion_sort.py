import array as arry
def insertion(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
 
arr = arry.array("i", [33, 47, 99, 2, 10, 444, 88, 77, 41])
insertion(arr)