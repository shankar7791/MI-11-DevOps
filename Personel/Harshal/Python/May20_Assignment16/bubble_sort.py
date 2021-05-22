import array as arr
a = arr.array("i", (89, 78, 66, 23, 5, 19, 6, 90))
print("Array Before Bubble Sort")
print(a)
print("\nSorting Array Using Bubble Sort")
for i in range(len(a)) :
    for j in range(0, len(a)-i-1):
        if a[j+1] < a[j] :
            a[j],a[j+1] = a[j+1],a[j]
    print(a)
print("\nArray After Bubble Sort")
print(a)