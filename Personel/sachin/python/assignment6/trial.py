def add_data() :
    matrix1 =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("enter 9 numbers for a matrix")
    for i in range(len(matrix1)) :
        for j in range(len(matrix1[0])) :
            matrix1[j]= int(input())



add_data()
for j in matrix1 :
    print(j)
    