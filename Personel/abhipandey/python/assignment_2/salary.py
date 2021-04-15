inc = int(input("enter the salary : "))
if inc <= 10000 :
    da = 0.8 * inc
    hra = 0.2 * inc
elif inc >= 20000 :
    da = 0.95 * inc 
    hra = 0.3 * inc
else :
    da = 0.25 * inc 
    hra = 0.9 * inc
gross = inc + da + hra
print("gross salary is :" , gross)