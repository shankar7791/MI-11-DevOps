#Prog 3.2. Write a Python program to construct the following pattern, using a nested while loop.
   #     *
   #     * *
    #    * * *
    #    * * * *
     #   * * * * *
    #    * * *
     #   * *
    #    *


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')