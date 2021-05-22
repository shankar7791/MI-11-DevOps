import array as arr
x = arr.array("i", (66, 50, 58, 888, 24, 36, 90))
print("Array Before Selection Sort")
print(x)
print("\nSorting Array Using Selection Sort")
for i in range(len(x)) :
    temp = i
    for j in range(i+1, len(x)):
        if x[j] < x[temp] :
            temp = j
    x[i],x[temp] = x[temp],x[i]
    print(x)
print("\nArray After Selection Sort")
print(x)