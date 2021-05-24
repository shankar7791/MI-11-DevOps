import array as arry
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
 
arr = arry.array("i", [14, 46, 43, 27, 57, 41, 45, 21, 70])
insertionSort(arr)