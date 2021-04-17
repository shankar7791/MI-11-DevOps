##Q1.Python Program to check number is positive, negative or zero

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

## Q2. Python program to check Leap year   

year = int(input("Enter a year: "))  
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

#Q3. Python program to find the largest number amongst the tree numbers.   

num1 = 7
num2 = 10
num3 = 20


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

# Q4. Write a program to check whether a number is divisible by 5 an 11 or not 

number = int(input(" Please Enter any Positive Integer : "))

if((number % 5 == 0) and (number % 11 == 0)):
    print("Given Number {0} is Divisible by 5 and 11".format(number))
else:
    print("Given Number {0} is Not Divisible by 5 and 11".format(number))

# Q5. Write a program to input any alphabets and check it is vowel or consonent    

ch=input("Please enter the character as you wish: ")


if(ch== 'a'or ch== 'A'or ch== 'e'or ch== 'E'or ch== 'i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
   print("The given character ",ch," is  the vowel")
else:
    print("The given character ",ch," is  consonant")

# Q6. Write a program to check  entered input is  alphabet digit or special character  
ch = input("Please Enter Any Character : ")
 
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is a Special Character")  

# Q7. Write a C program to input basic salary of an employee and calculate gross salary according to given conditions.  
    #  Basic Salary <= 10000 : HRA = 20%, DA = 80%
    #  Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
    #  Basic Salary >= 20001 : HRA = 30%, DA = 95%



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
  