import array as arr
a = arr.array("i", (89, 78, 66, 23, 5, 19, 6, 90))
print("Array Before Selection Sort")
print(a)
print("\nSorting Array Using Selection Sort")
for i in range(len(a)) :
    temp = i
    for j in range(i+1, len(a)):
        if a[j] < a[temp] :
            temp = j
    a[i], a[temp] = a[temp], a[i]
    print(a)
print("\nArray After Selection Sort")
print(a)