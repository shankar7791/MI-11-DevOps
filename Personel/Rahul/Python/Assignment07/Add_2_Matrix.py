a =[[1,5,3],
    [9,9,3],
    [8,8,7]]

b =[[2,7,2],
    [5,8,4],
    [6,8,6]]

r =[[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range (len(a)):
    for j in range (len(a[0])):
        r [i][j] = a[i][j] + b[i][j] 
for r in r:
    print(r)