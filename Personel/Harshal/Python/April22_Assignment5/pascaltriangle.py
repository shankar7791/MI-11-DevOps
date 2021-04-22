def fact(num) :
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial*i
    return factorial

n = 5

for i in range(n):
    for j in range(n-i+1) :
        print(end = " ")
    for k in range(i+1) :
        print(fact(i) // (fact(k) * fact(i - k)), end=" ")
    print()