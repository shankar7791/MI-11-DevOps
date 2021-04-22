height = float(input("enter the height in cm: "))
weight = float(input("enter the weight in kg: "))
bmi = weight/(height/100)**2
print("your body mass index is: " ,bmi)
if bmi <= 18.4:
    print("\n you are under weight. ")
elif bmi <= 24.9:
    print("\n you are normal weight.")
elif bmi <= 29.9:
    print("\n you are over weight.")
elif bmi <= 34.9:
    print("\n you are obese(class1). \n consult doctor immediately")
elif bmi <= 39.9:
    print("\n you are obese(class2).\n consult doctor immediately ")
else:
    print("\n you are obese(class3) \n consult doctor immediately")