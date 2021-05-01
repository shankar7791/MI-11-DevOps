#prog 5.1.Python Program to add two matrices using nested for loop.




row=int(input("enter raw: "))
col=int(input("enter col: "))
A=[]

for i in range(row):
    a=[]
    for j in range(col):
      a.append(int(input()))
    A.append(a)  

for i in range(row):
    for j in range(col):
        print(A[i][j],end=" ")
    print()


row1=int(input("enter raw1: "))
col2=int(input("enter col2: "))
B=[]

for i in range(row1):
    a=[]
    for j in range(col2):
      a.append(int(input()))
    B.append(a)  

for i in range(row1):
    for j in range(col2):
        print(B[i][j],end=" ")
    print()


result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(row):
   # iterate through columns
   for j in range(col):
       result[i][j] = A[i][j] + B[i][j]

for r in result:
   print(r)