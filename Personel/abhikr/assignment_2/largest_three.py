
#3.Python program to find the largest number amongst the three number

x=int(input("please enter first no "))
y=int(input("please enter second no "))
z=int(input("please enter third no "))
if x > y and x > z:
    print("largest no1 is",x)

elif y> x and y > z:
    print("largest no is",y)

else:
    print("largest no is",z)

