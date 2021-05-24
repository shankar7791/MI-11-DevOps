import array as arr

numarray = arr.array("i",[10, 5, 88, 99, 60])

fd = open("file.txt", "w")
for i in range(len(numarray)) :
    k = str(numarray[i])
    fd.write(k)
fd.close()

fd1 = open("file.txt", "r")
larr = fd1.read().split()
fd1.close()

print("Array before sorting: \n")
for i in numarray:
    print(i,end=" ")
for i in range(len(numarray)) :
    for j in range (len(numarray)) :
        if i<j :
            temp = numarray[i]
            numarray[i] = numarray[j]
            numarray[j] = temp



print("\nArray after sorting: \n")
for i in numarray :
    print(i, end= " ")
print("\n")