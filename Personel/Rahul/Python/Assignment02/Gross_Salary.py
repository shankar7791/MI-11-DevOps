basic = int(input("Enter The Basic Salary : "))
if basic <= 10000 :
    da = 0.8 * basic
    hra = 0.2 * basic
elif basic > 20000 :
    da = 0.9 * basic
    hra = 0.25 * basic
else :
    da = 0.95* basic
    hra = 0.30 * basic
gross = basic + da + hra
print("Gross Salary is :" ,gross)