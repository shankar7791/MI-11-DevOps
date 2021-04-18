
#7 : Write a C program to input basic salary of an employee and calculate gross salary according to given conditions.
                      #Basic Salary <= 10000 : HRA = 20%, DA = 80%
                      #Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
                      #Basic Salary >= 20001 : HRA = 30%, DA = 95%

basic_salary=int(input("Enter the basic salary "))
if basic_salary <= 10000 :
    gross_salary=basic_salary*20*80
    print('gross_salary',gross_salary)

elif basic_salary >=20001:
    gross_salary=basic_salary*30*95
    print('gross_salary',gross_salary)

else :
     gross_salary=basic_salary*25*90
     print('gross_salary',gross_salary)
