a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[6,7,8],
     [7,8,9],
     [1,4,5]]

r = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        r[i][j] = a[i][j] + b[i][j]
    
for res in r :
    print(res)