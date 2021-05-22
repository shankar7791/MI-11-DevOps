import array as arr
r = arr.array("i", (66, 55, 44, 22, 33, 99, 88, 111))
print("Array Before Bubble Sort")
print(r)
print("\nSorting Array Using Bubble Sort")
for i in range(len(r)) :
    for j in range(0, len(r)-i-1):
        if r[j+1] < r[j] :
            r[j],r[j+1] = r[j+1],r[j]
    print(r)
print("\nArray After Bubble Sort")
print(r)