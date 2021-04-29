def recfib(a):
    if a <=1:
        return a
    else:
        return(recfib(a-1))
n_terms = 10
if n_terms <= 0:
    print("print invalid input.")
else:
    print("fibonacci series: ")
    for i in range(n_terms):
        print(recfib(i))