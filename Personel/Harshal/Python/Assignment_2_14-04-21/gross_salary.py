sal = int(input("Enter your basic salary : "))
if sal <= 10000 :
    da = 0.8 * sal
    hra = 0.2 * sal
elif sal > 20000 :
    da = 0.95 * sal
    hra = 0.3 * sal
else :
    da = 0.9 * sal 
    hra = 0.25 * sal
gross = sal + da + hra
print(f"Gross Salary is {gross} .")