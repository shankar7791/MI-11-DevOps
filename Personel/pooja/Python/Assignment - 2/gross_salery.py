basic = int(input("Enter Basic Salary : "))
if basic <= 10000 :
    DA = 0.8 * basic
    HRA= 0.2 * basic
elif basic > 20000 :
    DA  = 0.9 * basic
    HRA = 0.25 * basic
else :
    DA = 0.95* basic
    HRA = 0.30 * basic
gross = basic + DA + HRA
print("Gross Salary is :" ,gross)

