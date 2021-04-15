#1.python Program to Add two numbers.

def addition_of_num(num1,num2):
    print("addition of given number is ",num1+num2)


num1=int(input("please enter first number to add"))
num2=int(input("please enter first number to add"))
addition_of_num(num1,num2)




#2.Python program to check Leap year

year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))




#3.Python program to find the largest number amongst the tree number

num1=int(input("please enter the number the first"))
num2=int(input("please enter the number the second"))
num3=int(input("please enter the number the third"))
if num1 > num2 and num1 > num3:
    print("largest number is",num1)

elif num2 > num1 and num2 > num3:
    print("largest number is",num2)

else:
    print("largest number is",num3)


#4.write a program to check whether a number is divisible by 5 an 11 or not 
num=int(input("please enter the numbe"))
if num%5==0 and num%11==0:
    print("the givn number is divisible by 5 an 11")
else:
    print("the given number is not divisble by 5 and 11")




#5.Write a program to input any alphabets and check it is vowel or consonent
vowel=['a','e','i','o','u']
#consonent=['b','c','d','f','g','h','j','k','l''m','n','p','q','r','s','t','v','w''x','y','z']
alpha=input("please enter the alphabets:--")
if alpha in vowel:
    print("the given alphabhet is vowel")
else:
    print("the given aphabet is consonent")



#6.Write a program to check  entered input is  alphabet digit or special character
special_character=['!','~','@','#','$','%','^','&','*','?','/']
inpt=input("please enter the ")
if inpt in special_character:
    print("the given input is special charector")
else:
    print('the given input is aphadigits')




#7 : Write a C program to input basic salary of an employee and calculate gross salary according to given conditions.
                      #Basic Salary <= 10000 : HRA = 20%, DA = 80%
                      #Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
                      #Basic Salary >= 20001 : HRA = 30%, DA = 95%

besic_salary=int(input("please enter the besic sallary"))
if besic_salary <= 10000 :
    gross_salary=besic_salary*20*80
    print('gross_salary',gross_salary)

elif besic_salary >=20001:
    gross_salary=besic_salary*30*95
    print('gross_salary',gross_salary)




#8 write python program to check positive and negtive number or zero
num=int(input('please enter the number:-'))
if num>0:
    print("the enter number is Positive number")

elif num<0:
    print("the enter number is Negative number")

else:
    print("zero")




#9. Python Program to find Square root of number

num=int(input("please enter the number"))
num_sqrt = num**0.5
print('The square root of num is ',num_sqrt)

#10.Python Program to calculate area of Triangle
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is',area)



#11.Python Program to swap two variables
a=10
b=20
b=b-a
a=a+b
print("after swaping the value of a and b are",a,b)




#12 Python Program to genrate random number
import random
for i in range(0,70):
    print(random.randint(1,100))





#13 Python Program to Convert Celcious to Farenheight
#celsius * 1.8 = fahrenheit - 32
celsius=32.5
fahrenheit = (celsius * 1.8) + 32
print("the convesrtion of  32.5 celsius into Farenheight is::---",fahrenheit)






