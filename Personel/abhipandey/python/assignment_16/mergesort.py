import array as arr
def mergesort(lis):
    print("split ",lis)
    if len(lis)>1:
        mid = len(lis)//2
        lh = lis[:mid]
        rh = lis[mid:]

        mergesort(lh)
        mergesort(rh)
        i=j=k=0       
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                lis[k]=lh[i]
                i=i+1
            else:
                lis[k]=rh[j]
                j=j+1
            k=k+1

        while i < len(lh):
            lis[k]=lh[i]
            i=i+1
            k=k+1

        while j < len(rh):
            lis[k]=rh[j]
            j=j+1
            k=k+1
    print("merge ",lis)

arry = arr.array("i",[33, 47, 99, 2, 10, 444, 88, 77, 41])
mergesort(arry)
print(arry)