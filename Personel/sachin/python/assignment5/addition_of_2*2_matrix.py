matrix1 = [[15, 52, -3], [4, 5, 6], [-4000, 23, 62]]

matrix2 =  [[-1, 42, 3], [0, 45, 66], [77, -8, 11]]

addition_matrix =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Matrix 1 is : \n")

for i in matrix1 :
    print(i)

print("\n Matrix 2 is : \n")

for j in matrix2 :
    print(j)
    
i=0
for i in range(len(matrix1)) :
    for j in range(len(matrix1[0])) :
        addition_matrix[i][j] = matrix1[i][j] + matrix2[i][j] 

print("\nAddition of Two Matrices is : \n")

for k in addition_matrix :
    print(k)