import array as arr
def mergeSort(lis) :
    print("Split ", lis)
    if len(lis) > 1 :
        mid = len(lis) // 2
        lh = lis[:mid]
        rh = lis[mid:]

        mergeSort(lh)
        mergeSort(rh)
        i = j = k = 0       
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                lis[k] = lh[i]
                i += 1
            else:
                lis[k] = rh[j]
                j += 1
            k += 1

        while i < len(lh):
            lis[k] = lh[i]
            i += 1
            k += 1

        while j < len(rh):
            lis[k] = rh[j]
            j += 1
            k += 1
    print("Merge ", lis)

arry = arr.array("i", [14, 46, 43, 27, 57, 41, 45, 21, 70])
mergeSort(arry)
print(arry)
