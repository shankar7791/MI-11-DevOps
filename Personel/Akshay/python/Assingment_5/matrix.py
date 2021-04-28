#Python Program to add two matrices using nested for loop.
x = [[3, 2, 3],
    [4, 6, 6],
    [7, 8, 9]]

y = [[7, 7, 3],
    [4, 5, 7],
    [7, 8, 9]]

z = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

print("Matrix 1 is : ")

for i in x :
    print(i)

print("Matrix 2 is : ")

for j in y :
    print(j)

for i in range(len(x)) :
    for j in range(len(x[0])) :
        z[i][j] = x[i][j] + y[i][j] 

print("Addition of Two Matrices is : ")

for k in z :
    print(k)