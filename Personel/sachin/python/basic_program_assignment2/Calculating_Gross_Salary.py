salary = int(input("Enter your basic salary : "))
if salary <= 10000 :
    DA = 0.8 * salary
    HRA = 0.2 * salary
elif salary > 20000 :
    DA = 0.95 * salary
    HRA = 0.3 * salary
else :
    DA = 0.9 * salary 
    HRA = 0.25 * salary
gross_salary = salary + DA + HRA
print(f"Gross Salary is {gross_salary} .")