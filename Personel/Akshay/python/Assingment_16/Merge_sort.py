def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        Left  = arr[:mid]
        Right = arr[mid:]
        merge_sort(Left)
        merge_sort(Right)
        i = j = k = 0
        while i < len (Left) and j < len(Right):
            if Left [i] < Right[j]:
                arr[k] = Left[i]
                i+=1
            else:
                arr[k] = Left [i]
                i +=1
                k +=1
        while j < len (Right):
              arr[k] = Right[j]
              j +=1
              k +=1
def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
    
if __name__ == "__main__":
    arr = [44, 55, 33, 57, 89, 77, 63, 56, 79]
    print("Given arry is ", end = "\n")
    printlist(arr)
    merge_sort(arr)
    print("sorted arry is :",end="\n")
    printlist(arr)
